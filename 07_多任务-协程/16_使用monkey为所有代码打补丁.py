from gevent import monkey
import gevent
import time

monkey.patch_all()  # 将程序中耗时操作的代码，换成gevent中自己实现的模块


def f(n, name):
    for i in range(n):
        print(name, i)
        time.sleep(0.5)


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(f, 5, "worker1"),
        gevent.spawn(f, 5, "worker2"),
        gevent.spawn(f, 5, "worker3"),
    ])
