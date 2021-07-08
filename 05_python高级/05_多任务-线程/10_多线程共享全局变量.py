import threading
import time

num = 100


def test1():
    global num
    for i in range(5):
        num += 1
        print("test1 %d" % num)
        time.sleep(1)


def test2():
    for i in range(5):
        print("test2 %d" % num)
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("main thread %d" % num)

# test1 101
# test1 102
# test2 102
# test1 103
# test2 103
# main thread 103
# test1 104
# test2 104
# test1 105
# test2 105
# test2 105
