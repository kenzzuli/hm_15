class Cat:
    def __init__(self, name):
        self.name = name
        print("%s is coming!" % self.name)

    def __del__(self):
        print("%s is gone!" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "I am %s" % self.name


# tom是一个全局变量
cat1 = Cat("Tom")
print(cat1)
