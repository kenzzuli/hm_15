import time
from greenlet import greenlet


def worker1():
    while True:
        print("--1--")
        time.sleep(0.1)
        gr2.switch()  # 切换


def worker2():
    while True:
        print("--2--")
        time.sleep(0.1)
        gr1.switch()  # 切换


if __name__ == '__main__':
    # gr1和gr2都是全局变量
    gr1 = greenlet(worker1)
    gr2 = greenlet(worker2)

    # 切换到gr1中运行
    gr1.switch()

# --1--
# --2--
# --1--
# --2--
# --1--
# ...
