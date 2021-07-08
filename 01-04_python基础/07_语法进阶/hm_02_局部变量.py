# 局部变量的作用域、生命周期
def demo_01():
    # 出生：执行下方代码之后，才会被创建
    # 死亡：函数执行结束后
    num = 1
    print("num的值为%d" % num)


def demo_02():
    num = 99
    print("demo02==> %d" % num)
    pass


# 在函数内部定义的变量(局部变量），仅能在当前函数内部使用，不能在其他位置使用
# print(num)
# demo_02()

demo_01()
demo_02()
