import re

# 在一般的字符串中\n整体表示一个换行符，
# 如果加上r，变成原始字符串，\n则分别表示\和n，为了在一般字符串中表示\，需要加一个\对\转义
print(r"\n" == "\\n")  # True
print(r"\n" == "\n")  # False

a = r"\n"
b = "\n"
print(len(a))  # 2
print(len(b))  # 1
print(a[0])  # 为\
print(b[0])  # 为换行符

# 如果不加r
print(re.findall("\n", "\n"))  # ['\n']
print(re.findall("\\n", "\n"))  # ['\n']
print(re.findall("\\n", "\\n"))  # []
print(re.findall("\\\\n", "\\n"))  # ['\\n']

print("*" * 50)
# 加r的效果在于，后面几个杠，前面写几个杠即可，无需考虑转义
print(re.findall(r"\n", "\n"))  # ['\n']
print(re.findall(r"\\n", "\\n"))  # ['\\n']
print(re.findall(r"\\\n", "\\\n"))  # ['\\\n']

print(r"\n" == "\\n")  # True
print(re.findall(r"\n", "\\n"))  # []
