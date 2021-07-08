# 装饰有返回值的函数
# 不论被装饰函数是否有return，都可以在装饰器加上return，这才是通用的装饰器模板
def set_func(func):
    def call_func(*args, **kwargs):
        print("权限验证1")
        return func(*args, **kwargs)  # 这里加上return

    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("在test1中 num =", num)
    return 666


print(test1(10))
# 权限验证1
# 在test1中 num = 10
# 666