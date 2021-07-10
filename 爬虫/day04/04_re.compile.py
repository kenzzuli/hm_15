import re

a = "hello2world3"
# 提前编译，能提高运行效率
p = re.compile(r"\d")
print(p.findall(a))  # ['2', '3']
print(p.sub("_", a))  # hello_world_

# 如果想要更改匹配模式，需要在编译时提前指定
p2 = re.compile(r".", re.S)
print(p2.findall("\n"))  # ['\n']

# 如果编译时未指定，在匹配时指定，是无效的
p3 = re.compile(".")
print(p3.findall("\n", re.S))  # []


