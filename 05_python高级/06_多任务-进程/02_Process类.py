import multiprocessing
import os
import time


def run_proc(name, age, **kwargs):
    for i in range(9):
        print("child process, i={}, name={}, age={}, pid={}".format(i, name, age, os.getpid()))
        print(kwargs)
        time.sleep(0.3)


if __name__ == '__main__':
    p = multiprocessing.Process(target=run_proc, args=("p1", 111,), kwargs={"gender": "m"}, name="Child Process")
    p.start()
    # 查看子进程名称和id
    print("{}\t{}".format(p.name, p.pid))
    print("Main Process\t" + str(os.getpid()))
    # 主进程等待1s，然后立刻结束子进程
    time.sleep(1)
    print(p.is_alive())  # 查看子进程是否存活
    p.terminate()
    time.sleep(1)
    print(p.is_alive())
    p.join()  # 是否让主线程 等待子进程p执行结束或等待多少秒 后再继续向下执行
    for i in range(10):
        print(i)
