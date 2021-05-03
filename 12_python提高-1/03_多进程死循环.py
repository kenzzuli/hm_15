# 多进程死循环，有几个进程就跑满几个核
from multiprocessing import Pool


def test():
    while True:
        pass


if __name__ == '__main__':
    po = Pool()
    # 子进程死循环
    po.apply_async(test)
    # 主进程死循环
    while True:
        pass
