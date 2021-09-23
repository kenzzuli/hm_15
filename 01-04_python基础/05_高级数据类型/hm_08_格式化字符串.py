# 格式化字符串后的（）本质上就是元组
info = ("yang", 18, 1.85)
print("my name is %s, i am %d years old, and i am %.2f height" % info)

# 格式化字符串可与元组拼接 形成新的字符串
info_str = "my name is %s, i am %d years old, and i am %.2f height" % info
print(type(info_str))
print(info_str)


