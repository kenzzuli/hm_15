import re

a = re.search(r"\d+", "time:1000, sex:222")

print(a.group())
# 1000
# search不从头开始匹配，match从头开始匹配，search仅能查找到第一个满足正则的字符串，然后返回对象

b = re.findall(r"\d+", "time:1000, sex:222")
print(b)
# ['1000', '222']
# findall会以列表形式返回所有匹配的结果
