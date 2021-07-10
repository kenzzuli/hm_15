# 爬取豆瓣电影信息
import json
import requests


class DoubanSpider:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        self.categories = ["热门", "最新", "可播放", "经典", "冷门佳片", "动作", "喜剧", "爱情", "科幻", "悬疑",
                           "恐怖", "治愈" "欧美", "华语", "韩国", "日本", "豆瓣高分", "喜剧"]
        self.url_template = "https://movie.douban.com/j/search_subjects?type=movie&tag={}&page_limit=50&page_start={}"

    def parse_url(self, url):  # 请求url，获取响应
        return requests.get(url, headers=self.headers).content.decode()

    @staticmethod
    def get_movie_list(content_str):
        # 将json字符串转成python字典
        ret_dict = json.loads(content_str)
        # 提取电影字典组成的列表
        movie_list = ret_dict["subjects"]
        return movie_list

    @staticmethod
    def save_movie_list(movie_list, unique_movie_list):  # 提取保存数据
        with open("douban_4_unique.json", mode="a", encoding="utf8") as f:
            for movie_dict in movie_list:
                # 输出到控制台
                try:
                    movie_name = movie_dict["title"]
                    # 去重
                    if movie_name in unique_movie_list:
                        continue
                    else:
                        unique_movie_list.append(movie_name)
                        print(movie_name)
                        print(movie_dict["rate"])
                        print(movie_dict["url"])
                        print("*" * 50)
                except:
                    continue
                # 保存到文件
                f.write(json.dumps(movie_dict, ensure_ascii=False))
                f.write("\n")

    def run(self):  # 实现主要逻辑
        unique_movie_list = list()
        # 1.遍历电影类别
        for cat in self.categories:
            i = 0
            while True:
                # 2.构造url
                url = self.url_template.format(cat, i * 50)
                # 3.发送请求，获取响应
                content_str = self.parse_url(url)
                # 4.提取数据
                movie_list = self.get_movie_list(content_str)
                # 5.保存数据
                self.save_movie_list(movie_list, unique_movie_list)

                # 如果一页得到的数据小于50个，说明没了，退出循环
                if len(movie_list) < 50:
                    # print(i)
                    break
                # 每次循环 i都要加1
                i += 1
        print(len(unique_movie_list))


if __name__ == '__main__':
    douban_spider = DoubanSpider()
    douban_spider.run()
