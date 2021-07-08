class Cat:
    """this is a cat class"""

    def eat(self):
        # 哪个对象调用了该方法，self就是哪个对象的引用
        print("%s爱吃鱼" % self.name)

    def walk(self):
        print("%s爱闲逛" % self.name)


# create a Cat object
tom = Cat()
tom.eat()
tom.walk()
tom.name = "Tom"
