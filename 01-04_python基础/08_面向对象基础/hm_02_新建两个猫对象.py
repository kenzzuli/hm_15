class Cat:
    """this is a cat class"""

    def eat(self):
        print("小猫爱吃鱼")

    def walk(self):
        print("小猫爱闲逛")


# create a Cat object
tom = Cat()
tom.eat()
tom.walk()
print(tom)

# create another Cat object
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.walk()
print(lazy_cat)

cute_cat = lazy_cat
print(cute_cat)

