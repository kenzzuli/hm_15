# 优化，模拟真实场景
from multiprocessing import Process, Queue
import time


def download_from_web(q):
    # 这是总的数据
    data = list(range(100000))
    for i in data:
        # 模拟从网上一点点下载数据
        q.put(i, True)
        print("put %s" % i)


def process_data(q):
    # 延时，确保序列中要先有一些数据
    while q.empty():
        time.sleep(0.001)
    while True:
        try:
            # 模拟处理数据
            # 等待0.1s，如果还无法从序列读取数据，抛出异常
            # 0.1s足够另一个进程往序列中存入一些数据了
            i = q.get(True, 0.1)

            print("process %s" % i)
        except:
            break


if __name__ == '__main__':
    # 创建一个队列
    q = Queue()  # 不指定队列的最大长度
    # 创建两个进程
    p1 = Process(target=download_from_web, args=(q,))
    p2 = Process(target=process_data, args=(q,))
    # 启动下载进程
    p1.start()
    # 启动处理进程
    p2.start()
    # 主线程等待p1结束后再向下执行
    p1.join()
    # 主线程等待p2结束后再向下执行
    p2.join()
    print("所有数据处理完成")
