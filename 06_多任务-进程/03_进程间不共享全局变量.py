import multiprocessing
import time
import os

num_list = [11, 22]


def proc1():
    print("Child Process 1, pid={}, num_list={}".format(os.getpid(), num_list))
    for i in range(3):
        num_list.append(i)
        time.sleep(1)
        print("Child Process 1, pid={}, num_list={}".format(os.getpid(), num_list))


def proc2():
    for i in range(3):
        print("Child Process 2, pid={}, num_list={}".format(os.getpid(), num_list))
        time.sleep(1)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=proc1)
    p2 = multiprocessing.Process(target=proc2)
    p1.start()
    # p1.join() # 是否让主进程等待子进程p1运行结束后再向下执行

    p2.start()
