class Furniture:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "The area of %s is %.2f." % (self.name, self.area)
