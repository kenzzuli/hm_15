# 1.打开文件
file = open("README", "w")

# 2.读写文件
file.write("fuck you\n")
file.write("hi")

# 3.关闭文件
file.close()

# 打开文件
f = open("README", "w")

# 下面这些写操作的内容都会保存，因为打开的是同一个文件对象 还没关闭呢

f.write("hello python！\n")
f.write("今天天气真好")
f.write("""hello python！
今天天气真好""")
# 关闭文件
f.close()