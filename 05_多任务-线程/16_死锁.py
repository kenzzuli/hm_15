import threading
import time


class MyThread1(threading.Thread):
    def run(self):
        mutex_a.acquire()  # a上锁
        print(self.name)
        time.sleep(1)  # 延时，等待b被test2上锁
        mutex_b.acquire()  # b已经被上锁，需等待b解锁
        mutex_b.release()
        mutex_a.release()


class MyThread2(threading.Thread):
    def run(self):
        mutex_b.acquire()  # b上锁
        print(self.name)
        time.sleep(1)  # 延时，等待a被test2上锁
        mutex_a.acquire()  # a已经被上锁，需等待a解锁
        mutex_a.release()
        mutex_b.release()


mutex_a = threading.Lock()
mutex_b = threading.Lock()

if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
