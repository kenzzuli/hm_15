hello_str = "hello world"

# 1.判断是否以指定字符串开始
print(hello_str.startswith("hello"))  # 大小写敏感

# 2.判断是否以指定字符串结束
print(hello_str.endswith("orld"))

# 3.查找指定字符串
# index同样也可以查找指定的子字符串在大字符串中的索引
print(hello_str.find("wo"))
print("*" * 100)
print(hello_str.rindex('o'))
print(hello_str.index("o"))
print(hello_str.rindex("r"))
print(hello_str.index("r"))
print("*" * 100)

# find 如果指定的字符串不存在，会返回-1
# index 如果指定的字符串不存在，会报错
print(hello_str.find("abc"))
print(hello_str.index("abc"))

# 4.替换字符串
# replace方法执行后，会返回一个新的字符串，但不会修改原有字符串的内容！！！
print(hello_str.replace("ello", "i"))
print(hello_str)

hi_str = "Hi Are you happy?"
print(hi_str.lower().startswith("h"))
