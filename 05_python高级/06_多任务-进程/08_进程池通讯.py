import os
from multiprocessing import Pool, Manager
import time


def read(q):
    while not q.empty():
        print("pid:%s\tppid:%s\tget:%s" % (os.getpid(), os.getppid(), q.get(True)))


def write(q):
    data = list("FUCK")
    for i in data:
        q.put(i, True)
        print("pid:%s\tppid:%s\tput:%s" % (os.getpid(), os.getppid(), i))


if __name__ == '__main__':
    print("pid:%s\tstart"% os.getpid())
    # 使用Manager中的Queue
    q = Manager().Queue()
    po = Pool(3)
    # 先向序列写入数据
    po.apply_async(write, (q,))
    time.sleep(1)  # 等1s，让write完成写入
    po.apply_async(read, (q,))
    po.close()
    po.join()
    print("pid:%s\tend" % os.getpid())
