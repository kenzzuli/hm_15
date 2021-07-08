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

    # 子类拥有父类所有的属性和方法
    def bark(self):
        print("叫")


wangcai = Dog("旺财")
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()

