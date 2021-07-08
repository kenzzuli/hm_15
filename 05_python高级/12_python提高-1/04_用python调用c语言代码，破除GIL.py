# 使用python调用c语言代码，破除GIL
from ctypes import *
from threading import Thread

# 加载动态库
lib = cdll.LoadLibrary("./libdeadloop.so")

# 创建子线程，让其执行c语言写的函数，此函数是个死循环
t = Thread(target=lib.DeadLoop)
t.start()

# 主线程死循环
while True:
    pass
