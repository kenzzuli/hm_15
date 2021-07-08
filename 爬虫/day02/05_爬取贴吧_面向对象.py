import requests


class TiebaSpider:
    def __init__(self, tieba_name, num):
        self.tieba_name = tieba_name
        self.num = num
        self.url_template = "https://tieba.baidu.com/f?kw={}&ie=utf-8&tp=0&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    def get_url_list(self):  # 构造url列表
        url_list = list()
        for i in range(self.num):
            url_list.append(self.url_template.format(self.tieba_name, 50 * i))
        return url_list

    def parse_url(self, url):  # 发送请求，获取响应
        response = requests.get(url, headers=self.headers)
        print(response.url)
        return response.content.decode()

    def save_html(self, html_str, page_num):  # 保存
        with open("./tmp/{}-第{}页.html".format(self.tieba_name, page_num), "w", encoding="utf8") as f:
            f.write(html_str)

    def run(self):  # 实现主要逻辑
        # 1.构造url列表
        url_list = self.get_url_list()
        # 2.遍历，发送请求，获取响应
        for index, url in enumerate(url_list):
            html_str = self.parse_url(url)
            # 3. 保存
            self.save_html(html_str, index + 1)


if __name__ == '__main__':
    tieba = TiebaSpider("nba", 100)
    tieba.run()
