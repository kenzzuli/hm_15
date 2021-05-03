# 自定义一个容器用来存放数据，通过add方法向其中添加数据
class Mylist(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)


my_list = Mylist()
my_list.add(1)
my_list.add(2)
for i in my_list:
    print(i)
# TypeError: 'Mylist' object is not iterable
