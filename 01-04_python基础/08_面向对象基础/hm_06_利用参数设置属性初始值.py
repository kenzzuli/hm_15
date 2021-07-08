class Cat:
    def __init__(self, name="tom"):
        print("调用初始化方法")
        self.name = name

    def __del__(self):
        print("%s要死了" % self.name)

    def eat(self):
        print("%s eats fish" % self.name)


# 创建对象时，会自己调用初始化方法__init__
tom = Cat()
print(tom.name)
lucy = Cat("lucy")
print(lucy.name)
# del lucy