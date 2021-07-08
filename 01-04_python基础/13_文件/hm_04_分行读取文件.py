file = open("README")
# 使用循环，读取所有行
while True:
    text = file.readline()
    if text == "":
        break
    # if not text:
    #     print("")
    #     print(len(text))
    #     break
    # 读行时，每行已经包含\n换行
    # 通过分步调试可以看到，第一次text = "hello 1\n"
    print(text, end="")
file.close()
