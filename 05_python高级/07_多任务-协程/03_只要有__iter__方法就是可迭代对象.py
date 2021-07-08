# 只要有__iter__方法，就是可迭代对象
from collections import Iterable


class MyContainer(object):
    def __init__(self):
        self.list = []

    def add(self, num):
        self.list.append(num)

    def __iter__(self):
        return None


my_container = MyContainer()
print(isinstance(my_container, Iterable))  # True

# 但是要想真正迭代，还需要进一步实现__iter__方法
for i in my_container:
    print(i)
# TypeError: iter() returned non-iterator of type 'NoneType'
