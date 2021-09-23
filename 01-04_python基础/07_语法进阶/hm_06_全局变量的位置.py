# 全局变量定义在所有函数上方，就可以保证所有函数都能够正常访问每一个全局变量
num = 10


name = "xiaoming"
title = "SISU"


def demo():
    print("%d" % num)
    print("%s" % name)
    print("%s" % title)


# # 再定义一个全局变量
# name = "xiaoming"

demo()


# # 再定义一个全局变量
# title = "SISU"
