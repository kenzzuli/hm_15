import threading
import time


def test1(tmp):
    for i in range(5):
        tmp.append(33)
        print("test1 %s" % str(tmp))
        time.sleep(1)


def test2(tmp):
    for i in range(5):
        print("test2 %s" % str(tmp))
        time.sleep(1)


if __name__ == '__main__':
    num_list = [11, 22]
    # target指定 线程要执行的函数名
    # args指定 调用函数时，传递的参数
    t1 = threading.Thread(target=test1, args=(num_list,))
    t2 = threading.Thread(target=test2, args=(num_list,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("main  %s" % str(num_list))

# test1 [11, 22, 33]
# test1 [11, 22, 33, 33]
# test2 [11, 22, 33, 33]
# test1 [11, 22, 33, 33, 33]
# main  [11, 22, 33, 33, 33]
# test2 [11, 22, 33, 33, 33]
# test1 [11, 22, 33, 33, 33, 33]
# test2 [11, 22, 33, 33, 33, 33]
# test2 [11, 22, 33, 33, 33, 33]
# test1 [11, 22, 33, 33, 33, 33, 33]
# test2 [11, 22, 33, 33, 33, 33, 33]