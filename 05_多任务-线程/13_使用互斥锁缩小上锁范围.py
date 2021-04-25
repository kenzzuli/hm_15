import time
import threading

g_num = 0


def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("test1 %d" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("test2 %d" % g_num)


if __name__ == '__main__':
    start = time.time()
    mutex = threading.Lock()
    nums = 100000000
    t1 = threading.Thread(target=test1, args=(nums,))
    t2 = threading.Thread(target=test2, args=(nums,))
    t1.start()
    t2.start()
    # 让主线程等待，直到t1和t2运行结束
    while len(threading.enumerate()) > 1:
        time.sleep(0.01)
    print("main  %d" % g_num)
    end = time.time()
    print(end - start)

# 41.47571921348572