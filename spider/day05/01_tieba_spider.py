import requests
from lxml import etree
import json
import re


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=" + tieba_name + "&pn=0"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36"}
        self.url_template = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2"

    def parse_url(self, url):  # 发送请求，获取响应
        print(url)
        html_str = requests.get(url, headers=self.headers).content.decode()
        # 从html_str中提取body标签内的内容，<XML version><DOCTYPE><head>等标签无用，仅<body>内有用
        p = re.compile("<body.*?>(.*?)</body>", re.DOTALL)
        html_str = p.findall(html_str)[0]
        return html_str

    def process_list_html(self, html_str):  # 处理列表页
        html = etree.HTML(html_str)
        # "//div[contains(@class,'i')]"
        # div_list = html.xpath("//div[contains(@class,'i')]")
        div_list = html.xpath("//div[@class='i']|//div[@class='i x']")
        next_page_url = html.xpath("//a[text()='下一页']/@href")
        tmp_list = self.extract_title_and_url(div_list)
        # 下一页列表页的url需要拼接上http等信息
        next_page_url = self.url_template + next_page_url[0] if next_page_url else None
        return tmp_list, next_page_url

    def extract_title_and_url(self, div_list):  # 从div分组中提取帖子的标题和url
        tmp_list = list()
        for div in div_list:
            title = div.xpath("./a/text()")
            url = div.xpath("./a/@href")
            # title和url都是列表，从中取值，加上if else是为了防止报错，但从逻辑上讲，一个帖子肯定有标题和url
            title = title[0] if title else None
            # 此外每个帖子的url需要拼接上http等信息
            url = self.url_template + url[0] if url else None
            tmp_dic = dict()
            tmp_dic["url"] = url
            tmp_dic["title"] = title
            tmp_list.append(tmp_dic)
        return tmp_list

    def save_data(self, info_dict):  # 保存一个帖子的title、url、和image
        with open("{}吧.txt".format(self.tieba_name), mode="a", encoding="utf8") as f:
            f.write(json.dumps(info_dict, ensure_ascii=False, indent=2))
            f.write("\n")
        print("保存成功")

    def process_detail_html(self, detail_html):  # 处理详情页
        html = etree.HTML(detail_html)
        images = html.xpath("//img[@class='BDE_Image']/@src")
        next_detail_page_url = html.xpath("//a[text()='下一页']/@href")
        # 下一页详情页的url需要拼接上http等信息
        next_detail_page_url = self.url_template + next_detail_page_url[0] if next_detail_page_url else None
        return images, next_detail_page_url

    def run(self):
        # 1.获取起始url
        # 2.发送请求，获取响应
        html_str = self.parse_url(self.start_url)
        while True:
            # 3.提取数据
            # 3.1 提取列表页中的每个帖子的标题、每个帖子的url、下一页列表页的url
            info_dict_list, next_page_url = self.process_list_html(html_str)
            # 3.2 发送每个帖子url请求，获取详情页
            for info_dict in info_dict_list:
                detail_html = self.parse_url(info_dict["url"])
                temp_image_list = list()
                while True:
                    # 3.3 提取详情页中的图片和下一页详情页的url
                    images, next_detail_page_url = self.process_detail_html(detail_html)
                    # 3.4 保存图片到临时的列表
                    temp_image_list += images
                    if not next_detail_page_url:
                        break
                    # 3.5 重复
                    detail_html = self.parse_url(next_detail_page_url)
                # 3.4 保存一个帖子的所有图片
                info_dict["image"] = temp_image_list
                # 4.保存数据
                self.save_data(info_dict)
            if not next_page_url:
                break
            # 5.重复
            html_str = self.parse_url(next_page_url)


if __name__ == '__main__':
    tieba_spider = TiebaSpider("lol")
    tieba_spider.run()
