# 多线程死循环，多个线程累加占满多核cpu的一个核
import threading


# 子线程死循环
def test():
    while True:
        pass


if __name__ == '__main__':
    t1 = threading.Thread(target=test)
    t1.start()
    # 主线程死循环
    while True:
        pass
