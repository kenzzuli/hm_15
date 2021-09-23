# 打开文件
file = open("README")
# 读取文件内容
text = file.read()
print(text)
print(len(text))

print("*" * 50)
text2 = file.read()
print(text2)
print(len(text2))
# 关闭文件
file.close()
