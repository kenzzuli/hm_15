try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数："))

    # 使用8除以用户输入的整数并输出
    print(8/num)

except ValueError:
    print("请输入整数")
# 假如我们不知道会抛出哪些异常，可以这样来捕获
except Exception as result:
    print("未知错误 %s" % result)