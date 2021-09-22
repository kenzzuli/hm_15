import json
from pprint import pprint
from parse_url import parse_url

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
html = parse_url(url)

# json.loads将json字符串转成python类型
ret = json.loads(html)
pprint(ret)

# json.dumps把python类型转成json字符串,再讲字符串写入文件 编码为utf8,缩进两个字符
with open("douban.json", mode="w", encoding="utf8") as f:
    f.write(json.dumps(ret, ensure_ascii=False, indent=2))
# json.dump直接将python数据类型保存到类文件对象中
with open("douban2.json", mode="w", encoding="utf8") as f:
    json.dump(ret, f, ensure_ascii=False, indent=2)

# json.loads将json字符串转成python类型
with open("douban.json", mode="r", encoding="utf8") as f:
    tmp = f.read()
    ret = json.loads(tmp)
    print(ret)

# json.load提取类文件对象中的数据
with open("douban.json", mode="r", encoding="utf8") as f:
    ret = json.load(f)
    print(ret)

