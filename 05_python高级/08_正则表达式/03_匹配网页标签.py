# 需求：匹配出<html><h1>www.itcast.cn</h1></html>
import re

html = "<html><h1>www.itcast.cn</h1></html>"
# match是从头开始匹配
res = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", html)
print(res.group())

res_new = re.match(r"<(?P<t1>\w*)><(?P<t2>\w*).*</(?P=t2)></(?P=t1)>$", html)
print(res_new.group())