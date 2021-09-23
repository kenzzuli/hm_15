class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def bark(self):
        print("哮天犬汪汪汪！")

    def fly(self):
        print("飞")


xtq = XiaoTianQuan("哮天犬")
# 如果子类中重写了父类的一个方法，那么子类对象在调用该方法时，会执行子类中重写的方法。
xtq.bark()