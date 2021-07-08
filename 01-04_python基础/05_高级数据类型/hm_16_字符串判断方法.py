# 判断空白字符
space_str = "     \t \r \n"
print(space_str.isspace())
print("*" * 50)

# 判断字符串中是否包含数字

"""
三个函数的判断范围
isdecimal（仅阿拉伯数字） 
                    < isdigit（阿拉伯数字+ Unicode字符） 
                    < isnumeric（阿拉伯数字+Unicode字符串+汉字数字
"""
# 1> 都不能判断小数
# num_str = "1.1"
# 2> unicode字符串（无法通过键盘直接输入，但可以通过转义的方式输入）
# num_str = "⑴\u00b2"
# 3> 中文数字
num_str = "一千零一"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

