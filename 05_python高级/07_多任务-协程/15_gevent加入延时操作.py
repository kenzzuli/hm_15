import gevent
# import time


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)  # 必须是gevent中的延时，time中的延时不行，输出结果没有变化


if __name__ == '__main__':
    print("---1---")
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)
    print("---2---")
    g1.join()
    g2.join()
    g3.join()
