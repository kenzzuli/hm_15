import threading
import time


def test():
    for i in range(5):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    print("start")
    # 实例化thread之前的线程数
    print(threading.enumerate())
    t1 = threading.Thread(target=test)
    # 实例化thread之后的线程数
    print(threading.enumerate())
    t1.start()
    # 调用thread对象的start方法后的线程数
    print(threading.enumerate())
