class Cat:
    def __init__(self):
        print("调用初始化方法")
        self.name = "Tom"

    def eat(self):
        print("%s eats fish" % self.name)


# 创建对象时，会自己调用初始化方法__init__
tom = Cat()
print(tom.name)
tom.eat()
