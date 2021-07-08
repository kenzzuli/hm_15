# 对无参数无返回值的函数进行装饰
def set_func(func):
    def call_func():
        print("权限验证1")
        print("权限验证2")
        func()

    return call_func


@set_func
def test():
    print("原来的函数")


test()
# 权限验证1
# 权限验证2
# 原来的函数
