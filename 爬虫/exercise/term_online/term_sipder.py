import requests
import json
import os


class TermSpider:
    def __init__(self, term_list):
        self.term_list = term_list
        self.home_page = "https://www.termonline.cn/search?k={}"
        self.post_url = "https://www.termonline.cn/tm/api/tm/search"
        self.headers = {
            # 手机版也有htoken，规避不了
            # htoken通过js生成，这个需要破解 https://www.termonline.cn/static/js/chunk-273c3f4b.70214fa6.js
            "htoken": "MAuIPnKbjrdrrEWcAMhw6w==",
            "Referer": "https://www.termonline.cn/search?k=%E7%8C%AA",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",

        }
        self.post_data_template = {"k": "猪", "highlight": False, "pno": 1, "match": "1", "dbids": ["1"], "sdms": [],
                                   "gbnds": [], "warn": 0, "uuid": "1626282534772"}
        self.base_dir = "./data"
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)

    def parse_url(self, post_data):
        print(post_data)
        r = requests.post(self.post_url, json=post_data, headers=self.headers)
        return r.content.decode() if r.status_code == 200 else ""

    def get_post_data(self, term, page_num):
        post_dict = self.post_data_template.copy()
        # post_dict["k"] = term
        # post_dict["pno"] = page_num
        return post_dict

    def save_content(self, content, term, page_num):
        data = json.loads(content)
        print(data)
        # print(json.dumps(data, ensure_ascii=False, indent=2))
        file_name = "术语[{}]_第[{}]页.txt".format(term, page_num)
        with open(os.path.join(self.base_dir, file_name), mode="a", encoding="utf8") as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2))
        print("保存成功")

    def run(self):  # 实现主要逻辑
        # 拼接post数据
        for term in self.term_list:
            for page_num in range(1, 10):
                post_data = self.get_post_data(term, page_num)
                # 发送请求，获取响应
                content = self.parse_url(post_data)
                # 保存数据
                self.save_content(content, term, page_num)
                exit()


if __name__ == '__main__':
    term_list = ["菌", "素", "毒", "霉素", "菌素", "病毒", "细胞", "剂", "液", "唑胺", "培养基", "药", "脂", "醇", "生物", "膜", "病"]
    term_spider = TermSpider(term_list)
    term_spider.run()
