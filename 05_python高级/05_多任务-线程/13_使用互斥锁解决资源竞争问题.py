import time
import threading

g_num = 0


def test1(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("test1 %d" % g_num)


def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
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

# 11.37648606300354
