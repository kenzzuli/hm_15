import requests.utils
import urllib.parse

# url解码
str = "%E4%B8%AD%E5%9B%BD"
a = requests.utils.unquote(str)
print(a)
b = urllib.parse.unquote(str)
print(b)

# 中国
# 中国
