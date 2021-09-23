class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s在玩" % self.name)


class XiaoTianQuan(Dog):
    def game(self):
        print("%s在飞" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s和%s玩" % (self.name, dog.name))
        dog.game()


wc = Dog("旺财")
xtq = XiaoTianQuan("哮天犬")
els = Person("二郎神")

# 多态，让不同的对象调用相同的方法产生不同的结果
# 调用Dog类中的game()方法
els.game_with_dog(wc)
# 调用XiaoTianQuan类中的game()方法
els.game_with_dog(xtq)
