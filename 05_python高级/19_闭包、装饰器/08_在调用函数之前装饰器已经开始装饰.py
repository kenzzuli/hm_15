# 调用函数之前，装饰器已经开始装饰
def set_func(func):
    print("装饰器开始工作")
    def call_func(num):
        print("权限验证1")
        print("权限验证2")
        func(num)

    return call_func


@set_func
def test1(num):
    print("在test1中 num =", num)

# 装饰器开始工作