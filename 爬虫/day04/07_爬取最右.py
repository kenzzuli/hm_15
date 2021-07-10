import requests
import re
import json


class ZuiyouSpider:
    def __init__(self):
        self.url = "https://www.izuiyou.com/hot"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    def parse_url(self, url):  # 发送请求，获取相应
        return requests.get(url, headers=self.headers).content.decode()

    @staticmethod
    def get_jokes(html_str):  # 获取数据
        p = re.compile(r"""<div class="review" role="button" tabindex="0">(.*?)</div>""", re.S)
        joke_list = p.findall(html_str)
        return joke_list

    @staticmethod
    def save_jokes(joke_list):  # 保存数据
        with open("zuiyou.txt", mode="a", encoding="utf8") as f:
            for joke in joke_list:
                if joke:  # 不为空
                    print(joke)
                    f.write(json.dumps(joke, ensure_ascii=False))  # 这里将字符串转为json字符串再写入文件，其实可以不转直接写
                    f.write("\n")

    def run(self):
        # 1.start_url
        # 2.发送请求，获取相应
        html_str = self.parse_url(self.url)
        # 3.提取数据
        joke_list = self.get_jokes(html_str)
        # 4.保存数据
        self.save_jokes(joke_list)


if __name__ == '__main__':
    zuiyou_spider = ZuiyouSpider()
    zuiyou_spider.run()
