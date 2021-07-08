# 以只读方式打开README
file1 = open("README")
# 以只写方式打开README[bak] 如果文件存在就覆盖，不存在就创建
file2 = open("README[bak]", "w")


while True:
    text = file1.readline()
    if not text:
        break
    file2.write(text)
# 关闭两个文件对象
file1.close()
file2.close()
