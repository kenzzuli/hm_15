# 使用nonlocal修改闭包中的数据
def test1():
    x = 100

    def test2():
        nonlocal x  # 要修改x的值，必须加nonlocal
        print(x)
        x = 200
        print(x)

    return test2


t = test1()
t()
