class Animal:
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
        # 子类特有的需求
        print("哮天犬汪汪汪！")
        # 使用super().调用父类中封装的方法
        super().bark()
        # python 2.X 用法 使用父类名调用方法，不推荐 父类名.方法名(self)
        Dog.bark(self)
        # 如果不小心写成了当前子类名，会造成死循环
        # XiaoTianQuan.bark(self)
        # 其他子类代码
        print("@##@%#@%%")

    def fly(self):
        print("飞")


xtq = XiaoTianQuan("哮天犬")
# 如果子类中重写了父类的一个方法，那么子类对象在调用该方法时，会执行子类中重写的方法。
xtq.bark()
