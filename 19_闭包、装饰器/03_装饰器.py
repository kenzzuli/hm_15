def set_func(func):
    def call_func():
        print("权限验证1")
        print("权限验证2")
        func()

    return call_func


@set_func   # 等价于test = set_func(test)
def test():
    print("原来的函数")


# # 在不修改原来函数的基础上，使用闭包增加新的功能
# t = set_func(test)  # t指向call_func这一函数
# t()  # 调用t相当于调用call_func，执行两个权限验证，再调用func，func在set_func中已经传入，为test
#
# print("-" * 50)
# # 如果把t改成test，也行
# test = set_func(test)
# test()  # 调用新test函数，相当于先执行两个权限验证，再调用旧test函数
# # 这种情况就相当于装饰器了

test()

# 上面三种调用函数的输出结果都是一样的
# 权限验证1
# 权限验证2
# 原来的函数
