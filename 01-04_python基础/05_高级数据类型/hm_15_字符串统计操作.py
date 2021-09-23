hello_str = "hello hello"

# 统计字符串长度
print(len(hello_str))

# 统计子字符串出现的次数
print(hello_str.count("llo"))
# 如果子字符串不存在，不会报错，会返回0
print(hello_str.count("abc"))

# 子字符串出现的位置
print(hello_str.index("llo"))
# 如果子字符串不存在，会报错
# print(hello_str.index("abc"))
trans_dic={"I": "我",
           "U": "你",
           "O": "爱"}
trans_table = str.maketrans(trans_dic)
source_str = "IOU"
print(source_str.translate(trans_table))
print(source_str.center(100))
print(source_str.endswith("U"))
