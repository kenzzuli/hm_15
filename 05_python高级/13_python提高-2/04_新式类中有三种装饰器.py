# Python3中，默认继承object类，都是新式类
class Goods:
    @property
    def size(self):
        return 200

    @size.setter
    def size(self, value):
        print("set size to", value)

    @size.deleter
    def size(self):
        print("delete size")


g = Goods()
print(g.size)   # 执行@property修饰的size方法，并获取返回值
g.size = 100   # 执行@size.setter修饰的size方法，并将100赋值给方法的value参数
del g.size   # 执行@size.deleter修饰的size方法

# 200
# set size to 100
# delete size
