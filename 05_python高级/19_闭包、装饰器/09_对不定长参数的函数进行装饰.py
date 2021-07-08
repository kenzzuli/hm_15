# 装饰不定长参数的函数
# 实际上，无论被装饰的函数无参数、有定长参数、有不定长参数，都可以这样写
def set_func(func):
    def call_func(*args, **kwargs):  # 在函数定义中，表示接受不定长参数和关键字参数
        print("权限验证1")
        print("权限验证2")
        func(*args, **kwargs)  # 在函数调用中，表示拆包

    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("在test1中 num =", num)
    print("在test1中 args =", args)
    print("在test1中 kwargs =", kwargs)


test1(10, 20, 30, name="peter", sex="m")
# 权限验证1
# 权限验证2
# 在test1中 num = 10
# 在test1中 args = (20, 30)
# 在test1中 kwargs = {'name': 'peter', 'sex': 'm'}
