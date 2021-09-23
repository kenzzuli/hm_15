class Person:
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "the weight of %s is %.2f" % (self.name, self.weight)

    def eat(self):
        self.weight += 1

    def run(self):
        self.weight -= 0.5


person1 = Person("peter", 75.0)
print(person1)
person1.eat()
print(person1)
person1.run()
print(person1)
