# 实现真正的迭代器


class MyContainer(object):
    def __init__(self):
        self.list = []

    def add(self, num):
        self.list.append(num)

    def __iter__(self):  # 返回一个迭代器对象
        return MyContainerIterator(self)  # 将可迭代对象自身传给迭代器


# 实现迭代器类
class MyContainerIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.index = 0

    def __iter__(self):  # iter函数要求返回一个迭代器对象，所以可以返回迭代器本身
        return self

    def __next__(self):
        if self.index < len(self.obj.list):  # 如果索引不超过元素个数
            item = self.obj.list[self.index]  # 取元素
            self.index += 1  # 索引+1
            return item
        else:
            raise StopIteration


my_container = MyContainer()
my_container.add(1)
my_container.add(2)
my_container.add(3)
for i in my_container:
    print(i)
