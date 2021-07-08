import time
import threading

num = 0


def test(times):
    global num
    for i in range(times):
        num += 1
    print(num)


if __name__ == '__main__':
    start = time.time()
    times = 200000000
    t1 = threading.Thread(target=test, args=(times,))
    t1.start()
    while len(threading.enumerate()) > 1:
        time.sleep(0.01)
    end = time.time()
    print(end - start)
# 11.686645984649658
