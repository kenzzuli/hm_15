import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            print("I am {} at {}".format(self.name, i))  # self.name 可以查看当前线程的名字


if __name__ == '__main__':
    for i in range(5):
        my_thread = MyThread()
        my_thread.start()
