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

    def get_content_list(self, html_str):  # 提取数据
        content_list = list()
        html = etree.HTML(html_str)
        next_page_url = html.xpath("//a[text()='下一页']/@href")
        # 下一页列表页的url需要拼接上http等信息
        next_page_url = self.url_template + next_page_url[0] if next_page_url else None
        # 获取div分组
        div_list = html.xpath("//div[contains(@class,'i')]")
        # div_list = html.xpath("//div[@class='i']|//div[@class='i x']")
        for div in div_list:
            item = dict()
            title = div.xpath("./a/text()")
            url = div.xpath("./a/@href")
            # title和url都是列表，从中取值，加上if else是为了防止报错，但从逻辑上讲，一个帖子肯定有标题和url
            item["title"] = title[0] if title else None
            # 此外每个帖子的url需要拼接上http等信息
            item["url"] = self.url_template + url[0] if url else None
            item["images"] = self.get_image_list(item["url"])
            content_list.append(item)

        return content_list, next_page_url

    def save_content_list(self, content_list):  # 保存数据
        with open("./tmp/{}吧.txt".format(self.tieba_name), mode="a", encoding="utf8") as f:
            f.write(json.dumps(content_list, ensure_ascii=False, indent=2))
            f.write("\n")
        print("保存成功")

    def get_image_list(self, next_url):  # 获取一个帖子内的所有图片
        image_list = list()
        while next_url:
            # 1.发送请求
            detail_html_str = self.parse_url(next_url)
            # 2.提取数据
            detail_html = etree.HTML(detail_html_str)
            image_list += detail_html.xpath("//img[@class='BDE_Image']/@src")
            # 3.获取下一个url
            next_url = detail_html.xpath("//a[text()='下一页']/@href")
            # 下一页详情页的url需要拼接上http等信息
            next_url = self.url_template + next_url[0] if next_url else None
        return image_list

    def run(self):
        # 1.获取起始url
        next_url = self.start_url
        while next_url:
            # 2.发送请求，获取响应
            html_str = self.parse_url(next_url)
            # 3.提取数据 每个帖子的标题、url、image和下一页列表页的url
            content_list, next_url = self.get_content_list(html_str)
            # 4.保存数据
            self.save_content_list(content_list)


if __name__ == '__main__':
    # tieba_spider = TiebaSpider("李毅")
    tieba_spider = TiebaSpider("上外")
    tieba_spider.run()
