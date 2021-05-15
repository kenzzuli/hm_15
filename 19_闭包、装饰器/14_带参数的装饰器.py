# 带有参数的装饰器
def set_level(level):  # 保存一个级别信息level
    def set_func(func):  # 保存了一个函数引用func
        def call_func(*args, **kwargs):  # 可以用上面保存的level和func
            if level == 1:
                print("级别1验证")
            elif level == 2:
                print("级别2验证")
            return func(*args, **kwargs)

        return call_func

    return set_func


@set_level(1)  # 将set_level(1）执行的结果 即set_func 作为装饰器来装饰test1
def test1():
    print("--test1--")
    return "ok"


@set_level(2)
def test2():
    print("--test2--")
    return "ok"


print(test1())
print(test2())
# 级别1验证
# --test1--
# ok
# 级别2验证
# --test2--
# ok
