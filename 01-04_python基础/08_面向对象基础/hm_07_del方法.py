class Cat:
    def __init__(self, name):
        self.name = name
        print("%s is coming!" % self.name)

    def __del__(self):
        print("%s is gone!" % self.name)



# tom是一个全局变量
cat1 = Cat("Tom")
cat2 = Cat("Lucy")
# del关键字可以删除一个对象
del cat1
print("*" * 50)