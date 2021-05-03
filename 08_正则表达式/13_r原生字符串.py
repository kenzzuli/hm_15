import re


# 想要在字符串中表达反斜杠，需要转义
mm = "c:\\a.\\b\\c"
print(mm)
# c:\a.\b\c

# 如果不加r，需要对反斜杠转义，这样要写两个反斜杠。
print(re.match("c:\\\\a\\.", mm).group())
# c:\a.

# 加上r后表示原生字符串，一个反斜杠就是一个反斜杠，无需对反斜杠再次进行转义，能和mm保持一致
print(re.match(r"c:\\a\.", mm).group())
# c:\a.

