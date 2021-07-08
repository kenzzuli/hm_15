import time
import threading


def sing():
    for i in range(3):
        print("singing %d" % i)
        time.sleep(1)


def dance():
    for i in range(3):
        print("dancing %d" % i)
        time.sleep(1)


if __name__ == '__main__':
    print("----start---- :%s " % time.ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    print("----end---- : %s " % time.ctime())
