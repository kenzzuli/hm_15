# python2中，不继承object，则是经典类
class Goods:  # 如果不继承，类名后不必加括号
    @property
    def size(self):
        return 200

    # @size.setter
    # def size(self, value):
    #     print("set size")
    #
    # @size.deleter
    # def size(self):
    #     print("delete size")


g = Goods()
print(g.size)
# g.size = 100
# del g.size
