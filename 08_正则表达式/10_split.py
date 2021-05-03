import re

a = re.split(r":| ", "info:xiaozhang 33 shandong")
print(a)
# ['info', 'xiaozhang', '33', 'shandong']
# split根据匹配切割字符串，并返回一个列表
