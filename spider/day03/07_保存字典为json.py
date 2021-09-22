import json
from pprint import pprint
from parse_url import parse_url

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
html = parse_url(url)

# 将json字符串转成python类型
ret = json.loads(html)
pprint(ret)

# 将python类型保存为json, 保存为utf8,缩进两个字符
with open("douban.json", mode="w", encoding="utf8") as f:
    f.write(json.dumps(ret, ensure_ascii=False, indent=2))
# 写入文件时，dump方法更好用
with open("douban2.json", mode="w", encoding="utf8") as f:
    json.dump(ret, f, ensure_ascii=False, indent=2)
