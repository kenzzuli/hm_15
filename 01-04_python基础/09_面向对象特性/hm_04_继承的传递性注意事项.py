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


class Cat(Animal):
    def catch(self):
        print("抓老鼠")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("飞")


# 创建一个哮天犬对象
xtq = XiaoTianQuan("哮天犬")
xtq.eat()
xtq.bark()

# 哮天犬类不能继承猫类中的方法和属性
# xtq.catch()