import requests
import os


class TermSpider:
    def __init__(self, book_list):
        self.url_template = "https://www.termonline.cn/tmbook/1/{}/pages/{}.jpg"
        self.book_list = book_list
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
        self.base_dir = "./books"

    def download(self, book_name):
        for i in range(1, 1000):
            try:
                url = self.url_template.format(book_name, i)
                print(url)
                if not os.path.exists(os.path.join(self.base_dir, book_name)):
                    os.mkdir(os.path.join(self.base_dir, book_name))
                r = requests.get(url, headers=self.headers, stream=True)
                # 大文件下载
                save_file_name = os.path.join(self.base_dir, book_name, "{}.jpg".format(i))
                with open(save_file_name, mode="wb") as f:
                    if r.status_code == 200:
                        f.write(r.content)
                print("下载完成")
            except Exception as e:
                print(e)
                break

    def run(self):
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)
        for book_name in book_list:
            self.download(book_name)


if __name__ == '__main__':
    book_list = ["农学名词-第一版-1993",
                 "动物学名词-第一版-1996",
                 "土壤学名词-第一版-1998",
                 "医学名词-第一版"
                 ]
    spider = TermSpider(book_list)
    spider.run()
    # url = "https://www.termonline.cn/tmbook/1/%E5%8A%A8%E7%89%A9%E5%AD%A6%E5%90%8D%E8%AF%8D-%E7%AC%AC%E4%B8%80%E7%89%88-1996/pages/4.jpg"
    # book_name = "动物学名词-第一版-1996"
    # page_num = 4

    # spider.download_book(url, book_name, page_num)
