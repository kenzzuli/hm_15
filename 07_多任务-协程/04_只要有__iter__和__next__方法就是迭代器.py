# 只要有__iter__方法和__next__方法，就是迭代器
from collections import Iterable, Iterator
import time


class MyContainer(object):
    def __init__(self):
        self.list = []

    def add(self, num):
        self.list.append(num)

    def __iter__(self):  # 返回一个迭代器对象
        return MyContainerIterator()


class MyContainerIterator(object):
    def __iter__(self):
        pass

    def __next__(self):
        return 11


# 实例化一个可迭代对象
my_container = MyContainer()
# 获取可迭代对象的迭代器
my_container_iterator = iter(my_container)

# 判断一个对象是否是可迭代对象
print(isinstance(my_container, Iterable))  # True
# 判断一个对象是否是迭代器
print(isinstance(my_container_iterator, Iterator))  # True

# 迭代可迭代对象my_container时，会先调用my_container的__iter__方法获取迭代器my_container_iterator
# 然后不停调用迭代器的__next__方法，获取其返回值，作为每次迭代的i
for i in my_container:
    print(i)
    time.sleep(1)
# 会一直打印11
# 11
# 11
# 11
# 11
# 11
# 11
# ...
