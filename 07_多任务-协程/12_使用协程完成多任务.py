# 使用协程完成多任务
import time


def worker1():
    while True:
        print("--1--")
        time.sleep(0.1)
        yield


def worker2():
    while True:
        print("--2--")
        time.sleep(0.1)
        yield


if __name__ == '__main__':
    w1 = worker1()
    w2 = worker2()
    while True:
        next(w1)
        next(w2)

# --1--
# --2--
# --1--
# --2--
# --1--
# --2--
# ...
