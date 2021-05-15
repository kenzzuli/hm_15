# 用装饰器统计函数运行时间
import time


def set_func(func):
    def get_time():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("函数运行时间为: %f" % (stop_time - start_time))

    return get_time


@set_func
def test():
    for i in range(10000):
        pass


test()
# 函数运行时间为: 0.000197
