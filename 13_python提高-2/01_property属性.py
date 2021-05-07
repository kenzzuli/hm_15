class Goods(object):
    @property
    def size(self):
        return 100


apple = Goods()
print(apple.size)
