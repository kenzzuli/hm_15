# 多个装饰器装饰同一个函数
def dec_1(func):
    print("装饰1")

    def call_func(*args, **kwargs):
        print("这里是装饰1")
        return func(*args, **kwargs)

    return call_func


def dec_2(func):
    print("装饰2")

    def call_func(*args, **kwargs):
        print("这里是装饰2")
        return func(*args, **kwargs)

    return call_func


@dec_1
@dec_2
def test1(num, *args, **kwargs):
    print("在test1中 num =", num)
    return 666


ret = test1(100)
print(ret)
# 装饰时，先装饰离函数最近的dec2，再装饰离函数远点的dec1
# 调用时，从最外层调，先执行dec1中的call_func，在其中调用func，func执行dec2中的call_func，在其中执行原来的test1函数，
# test1的返回值传给dec2中的call_func， call_func将返回值传给dec1中的call_func，call_func将返回值传给ret
# 装饰2
# 装饰1
# 这里是装饰1
# 这里是装饰2
# 在test1中 num = 100
# 666
