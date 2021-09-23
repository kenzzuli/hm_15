class Person:
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "the weight of %s is %.2f" % (self.name, self.weight)

    def eat(self):
        print("%s loves eating!" % self.name)
        self.weight += 1

    def run(self):
        print("%s loves running!" % self.name)
        self.weight -= 0.5


stu1 = Person("Ken", 100)
stu2 = Person("Karen", 65)
stu1.run()
stu1.eat()
print(stu1)
stu2.run()
stu2.eat()
print(stu2)


