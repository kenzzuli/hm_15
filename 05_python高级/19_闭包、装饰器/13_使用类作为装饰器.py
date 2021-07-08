# 使用类作为装饰器
class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("这里是装饰器添加的功能...")
        return self.func()


@Test  # 相当于 get_str = Test(get_str)
def get_str():
    return "hello"


print(get_str())  # 此时get_str是一个对象，对象后加括号，需要实现call方法

# 这里是装饰器添加的功能...
# hello
