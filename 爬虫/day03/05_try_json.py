import json
from parse_url import parse_url

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
html = parse_url(url)

# 将json字符串转成python类型
ret = json.loads(html)
print(ret)
