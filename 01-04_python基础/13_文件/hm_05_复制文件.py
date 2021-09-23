# 以只读方式打开README
file1 = open("README")
# 以只写方式打开README[bak] 如果文件存在就覆盖，不存在就创建
file2 = open("README[bak]", "w")
# 将从文件对象file1中读到的内容写入文件对象file2中
file2.write(file1.read())
# 关闭两个文件对象
file1.close()
file2.close()
