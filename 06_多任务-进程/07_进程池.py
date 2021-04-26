from multiprocessing import Pool
import os
import time
import random


def worker(msg):
    t_start = time.time()
    print("%d开始执行，进程号为%s" % (msg, os.getpid()))
    # 随机休眠0-1秒
    time.sleep(random.random())
    t_stop = time.time()
    print("%d执行完毕，耗时%.2f" % (msg, t_stop - t_start))


if __name__ == '__main__':
    print("---start---")
    # 实例化一个进程池，最大进程数为4
    po = Pool(4)
    for i in range(10):
        # Pool().apply_async(要调用的目标, (传递给目标的参数元组, ))
        # 每次循环都会用空闲出来的子进程来调用目标
        po.apply_async(worker, (i,))
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()   # 主进程等待po中所有子进程运行结束后再向下执行
    print("---end---")
