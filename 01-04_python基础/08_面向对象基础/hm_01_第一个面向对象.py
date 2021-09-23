class Cat:
    """this is a cat class"""
    def eat(self):
        print("小猫爱吃鱼")

    def walk(self):
        print("小猫爱闲逛")


tom = Cat()
tom.eat()
tom.walk()
print(Cat.__doc__)
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.walk()
print(tom)
print("%x" % id(tom))
print(lazy_cat)
print("%x" % id(lazy_cat))

