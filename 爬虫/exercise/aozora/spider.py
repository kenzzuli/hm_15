import requests
from lxml import etree
from urllib.parse import urljoin
import time
import random
import os


class AozoraSpider:
    def __init__(self):
        self.home_page = "https://www.aozora.gr.jp/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
        self.base_dir = "./novels"
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)

    def parse_url(self, url):
        return requests.get(url, headers=self.headers).content

    def download(self, url, file_name):  # 下载
        try:

            all_files = os.listdir(self.base_dir)
            print("正在下载小说: [{}]".format(file_name))
            # 有些文件名中包含/，会报错，要将/替换掉
            file_name = file_name.replace(r"/", "")
            if file_name in all_files:
                print("[{}]已存在，跳过！".format(file_name))
                return
            r = requests.get(url, headers=self.headers, stream=True)

            # 大文件下载
            with open(os.path.join(self.base_dir, file_name), mode="wb") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print("下载完成")
            print("随机休息1-3秒，防止被对方发现我们是爬虫")
            time.sleep(random.randint(1, 3))
        except Exception as e:
            self.write_exception(e)

    def get_cat_url_list(self):
        try:
            # 1.url为home_page
            # 2.发送请求，获取响应
            html_str = self.parse_url(self.home_page)
            # 3.提取url
            html = etree.HTML(html_str)
            url_list = html.xpath("//table[@summary='作品リスト']//td/a/@href")
            url_list = [urljoin(self.home_page, i) for i in url_list if not i.startswith("http")]
            # 4.返回
            return url_list
        except Exception as e:
            self.write_exception(e)

    def get_novel_detail_url_list(self, url):
        try:
            print("正在获取该页的所有小说的url: ", url)
            html_str = self.parse_url(url)
            html = etree.HTML(html_str)
            novel_detail_url_list = html.xpath("//td[@valign='top']/a/@href")
            novel_detail_url_list = [urljoin(url, i) for i in novel_detail_url_list if not i.startswith("http")]
            return novel_detail_url_list
        except Exception as e:
            self.write_exception(e)

    def get_all_page_url_list(self, url):
        try:
            print("正在获取该分类的所有页的url: ", url)
            html_str = self.parse_url(url)
            html = etree.HTML(html_str)
            all_page_url_list = html.xpath("//center//table//td[@valign='bottom'][@align='right']/a/@href")
            all_page_url_list = [urljoin(self.home_page, i) for i in all_page_url_list if not i.startswith("http")]
            all_page_url_list.append(url)
            return all_page_url_list
        except Exception as e:
            self.write_exception(e)

    def get_download_url(self, url):
        try:
            print("正在获取该小说的下载地址:", url)
            html_str = self.parse_url(url)
            html = etree.HTML(html_str)
            download_url = html.xpath("//a[contains(@href, '.zip')]/@href")
            if not download_url:
                with open("./no_zip_file.log", mode="a", encoding="utf8") as f:
                    f.write(url + "\n")
                return None, None

            download_url = download_url[0] if download_url[0].startswith("http") else urljoin(url, download_url[0])
            file_name = html.xpath("//a[contains(@href, '.zip')]/text()")[0]
            return download_url, file_name
        except Exception as e:
            self.write_exception(e)

    def write_exception(self, e):
        with open("exception.log", mode="a", encoding="utf8") as f:
            f.write(str(e) + "\n")

    def run(self):  # 实现主要逻辑
        # 获取分类url
        cate_url_list = self.get_cat_url_list()
        # 遍历每个分类
        for cate_url in cate_url_list:
            # 获取每个分类的所有页的url
            all_page_url_list = self.get_all_page_url_list(cate_url)
            if not all_page_url_list:
                continue
            # 遍历每个分类的所有页
            for page_url in all_page_url_list:
                # 获取每个分类的所有页上的所有小说详情页
                novel_detail_url_list = self.get_novel_detail_url_list(page_url)
                if not novel_detail_url_list:
                    continue
                # 遍历小说详情页
                for novel_detail_url in novel_detail_url_list:
                    # 获取下载链接
                    download_url, file_name = self.get_download_url(novel_detail_url)
                    # 下载
                    if not download_url:
                        continue
                    self.download(download_url, file_name)


if __name__ == '__main__':
    spider = AozoraSpider()
    spider.run()
