import multiprocessing
import os
import time


def run_proc():
    """子进程要执行的代码"""
    print("child process " + str(os.getpid()))
    while True:
        print("--2--")
        time.sleep(1)


if __name__ == '__main__':
    p = multiprocessing.Process(target=run_proc)
    print("main process " + str(os.getpid()))
    p.start()
    while True:
        print("--1--")
        time.sleep(1)
