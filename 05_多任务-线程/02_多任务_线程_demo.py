import time
import threading


def dance():
    for i in range(5):
        print("跳舞 %d" % i)
        time.sleep(1)


def sing():
    for i in range(5):
        print("唱歌 %d" % i)
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=dance)
    t2 = threading.Thread(target=sing)
    t1.start()
    t2.start()