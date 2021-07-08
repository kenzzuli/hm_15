# 对多个函数进行装饰
def set_func(func):
    def call_func(num):
        print("权限验证1")
        print("权限验证2")
        func(num)

    return call_func


@set_func
def test1(num):
    print("在test1中 num =", num)


@set_func
def test2(num):
    print("在test2中 num =", num)


test1(3)
test2(4)
# 权限验证1
# 权限验证2
# 在test1中 num = 3
# 权限验证1
# 权限验证2
# 在test2中 num = 4
