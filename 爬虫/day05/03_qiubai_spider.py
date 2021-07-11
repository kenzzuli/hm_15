from lxml import etree
import requests
import json


class QiubaiSpider:
    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/text/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
        self.template_url = "https://www.qiushibaike.com"

    def parse_url(self, url):  # 发送请求获取响应
        print(url)
        return requests.get(url, headers=self.headers).content

    def get_content_list(self, html_str):  # 获取数据
        content_list = list()
        html = etree.HTML(html_str)
        # 获取下一页url
        # "//span[@class='next']/@href"
        next_url = html.xpath("//span[contains(text(), '下一页')]/../@href")
        next_url = self.template_url + next_url[0] if next_url else None
        # 获取结果分组
        div_list = html.xpath("//div[contains(@class, 'article block untagged mb15 typs')]")
        for div in div_list:
            item = dict()
            # 作者信息
            author = dict()
            author_name = div.xpath("./div[@class='author clearfix']//h2/text()")
            author_img = div.xpath("./div[@class='author clearfix']//img/@src")
            author_gender = div.xpath(".//div[contains(@class, 'articleGender')]/@class")
            author_age = div.xpath(".//div[contains(@class, 'articleGender')]/text()")
            author["author_name"] = author_name[0].strip() if author_name else None
            author["author_img"] = "https:" + author_img[0].split("?imageView")[0] if author_img else None
            author["author_gender"] = author_gender[0].split()[-1][:-4] if author_gender else None
            author["author_age"] = author_age[0] if author_age else None
            item["author"] = author
            # 笑话
            content = div.xpath(".//div[@class='content']/span/text()")
            item["content"] = "\n".join(content).strip() if content else None
            # 当前点赞数和评论数
            status = dict()
            vote_number = div.xpath("./div[@class='stats']/span[@class='stats-vote']/i/text()")
            comment_number = div.xpath("./div[@class='stats']/span[@class='stats-comments']//i[@class='number']/text()")
            status["vote_number"] = vote_number[0] if vote_number else None
            status["comment_number"] = comment_number[0] if comment_number else None
            item['status'] = status
            # 最佳评论者、最佳评论、最佳评论点赞数
            comment = dict()
            best_commenter = div.xpath("./a[@class='indexGodCmt']//span[@class='cmt-name']/text()")
            best_comment = div.xpath("./a[@class='indexGodCmt']//div[@class='main-text']/text()")
            best_comment_like_number = div.xpath(
                "./a[@class='indexGodCmt']//div[@class='main-text']/div[@class='likenum']/text()")
            comment["best_commenter"] = best_commenter[0].strip()[:-1] if best_commenter else None
            comment["best_comment"] = best_comment[0].strip() if best_comment else None
            comment["best_comment_like_number"] = "".join(
                best_comment_like_number).strip() if best_comment_like_number else None
            item["comment"] = comment
            content_list.append(item)

        return content_list, next_url

    @staticmethod
    def save_content_list(content_list):  # 保存数据
        with open("./tmp/qiubai.txt", mode="a", encoding="utf8") as f:
            f.write(json.dumps(content_list, ensure_ascii=False, indent=2))
            f.write("\n")
        print("保存成功")

    def run(self):  # 实现主要逻辑
        # 1.获取起始url
        next_url = self.start_url
        while next_url:
            # 2.发送请求获取响应
            html_str = self.parse_url(next_url)
            # 3.提取数据
            content_list, next_url = self.get_content_list(html_str)
            # 4.保存数据
            self.save_content_list(content_list)


if __name__ == '__main__':
    qiubai_spider = QiubaiSpider()
    qiubai_spider.run()
