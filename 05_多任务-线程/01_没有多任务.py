import time


def sing():
    for i in range(5):
        time.sleep(1)
        print("唱歌 %d" % i)


def dance():
    for i in range(5):
        time.sleep(1)
        print("跳舞 %d" % i)


def dance_and_sing():
    sing()
    dance()


if __name__ == '__main__':
    dance_and_sing()
