# 迭代器一定是可迭代对象，可迭代对象不一定是迭代器
# 可以将可迭代对象自身加上__next__方法变成迭代器，这样就不必再定义新的迭代器类了

class MyContainer(object):
    def __init__(self):
        self.list = []
        self.current_index = 0

    def add(self, num):
        self.list.append(num)

    def __iter__(self):  # 返回一个迭代器对象
        return self  # 返回自身即可

    def __next__(self):
        if self.current_index < len(self.list):
            item = self.list[self.current_index]
            self.current_index += 1
            return item
        else:
            self.current_index = 0  # 迭代结束，必须把索引重新归零
            raise StopIteration


my_container = MyContainer()
my_container.add(1)
my_container.add(2)
my_container.add(3)
for i in my_container:
    print(i)
for i in my_container:
    print(i)
