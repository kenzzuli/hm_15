class Test(object):
    def __call__(self, *args, **kwargs):
        print("调用call方法")


test = Test()  # 实例化对象
test()  # 对象后加()
# 调用call方法
