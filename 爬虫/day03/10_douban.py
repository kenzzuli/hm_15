# 爬取豆瓣电影评分
from parse_url import parse_url
import json

url_template = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start={}"

i = 0
while True:
    # 构造url
    url = url_template.format(i * 50)
    # 请求url
    json_str = parse_url(url)
    # 将json字符串转成python字典
    ret = json.loads(json_str)
    movie_dicts = ret["subjects"]
    # 遍历每个电影，提取数据
    for movie in movie_dicts:
        try:
            print(movie["title"])
            print(movie["rate"])
            print(movie["url"])
            print("*" * 50)
        except:
            continue

    # 如果一页得到的数据小于50个，说明没了，退出循环
    if len(movie_dicts) < 50:
        # print(i)
        break
    # 每次循环 i都要加1
    i += 1
