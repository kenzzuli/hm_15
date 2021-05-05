# 私有化
class Person(object):
    def __init__(self, name, age, sex):  # 魔法方法
        self.name = name
        self._age = age  # 私有属性，不被导入
        self.__sex = sex  # 私有属性，不被继承，所以子类中并无__sex属性

    def show_person(self):
        print(self.name, self._age, self.__sex)


class Student(Person):
    def construction(self, name, age, sex):
        self.name = name
        self._age = age
        self.__sex = sex

    def show_student(self):
        print(self.name, self._age, self.__sex)

    @staticmethod
    def debug():
        _Bug().show_bug()


# 私有类，当前模块可以使用，但其他模块无法导入
class _Bug(object):
    @staticmethod
    def show_bug():
        print("debug")


s1 = Student('jack', 25, 'M')
s1.show_person()  # 父类方法可以调用所有父类属性
# jack 25 M
print(s1._age)  # 子类中有_age属性
# 25

# print(s1.__sex) # 子类中没有__sex属性，何况就算有__sex属性，在类外面也无法访问
# AttributeError: 'Student' object has no attribute '__sex'
# print(s1._Student__sex)  # 在外面强制访问私有属性，发现子类确实没有继承父类的__sex属性
# AttributeError: 'Student' object has no attribute '_Student__sex'
# s1.show_student()  # 此时调用子类的方法要打印父类的私有属性，会报错，因为子类中没有__sex属性
# AttributeError: 'Student' object has no attribute '_Student__sex'

s1.construction('rose', 30, 'F')  # 通过construction方法，给子类的属性重新赋值，并且新建了一个和父类重名的__sex属性
print(s1._age)  # 子类继承了父类的_age属性，通过construction方法，给子类的_age属性重新赋值了
# 30
# print(s1.__sex) # 子类中有__sex属性，但子类的私有属性在外面无法访问
# AttributeError: 'Student' object has no attribute '__sex'
print(s1._Student__sex)  # 在外面强制访问私有属性，确实存在__sex属性
# F
s1.show_person()  # show_person调用的是父类的方法，使用的父类中的私有属性__sex，其值为初始化时的M
# rose 30 M
s1.show_student()  # show_student调用的子类的方法，使用的是子类中与父类重名的私有属性__sex，其值为construction时的F
# rose 30 F
Student.debug()  # 在同一个模块中可以调用私有类
# debug
