# 对有参数无返回值的函数进行装饰
def set_func(func):
    def call_func(num):  # 这里也要加上对应数量的参数
        print("权限验证1")
        print("权限验证2")
        func(num)  # 调用原来函数时，也要加上对应数量的参数

    return call_func


@set_func
def test(num):  # 原来函数有参数
    print("在原来函数中 num =", num)


test(3)
# 权限验证1
# 权限验证2
# 在原来函数中 num = 3
