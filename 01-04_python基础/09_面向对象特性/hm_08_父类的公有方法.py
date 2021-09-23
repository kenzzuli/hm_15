class A:
    def __init__(self):
        self.num1 = 1
        self.__num2 = 2

    def __test(self):
        print("A类私有方法")
        print(self.__num2)

    def test(self):
        print("*" * 50)
        print("A类公共方法")
        # 子类对象可以通过调用父类的公共方法来间接访问父类的私有属性和私有方法
        print(self.__num2)
        self.__test()
        print("*" * 50)


class B(A):
    def demo(self):
        # 1.无法访问父类的私有属性
        # print(self.__num2)
        # 2.无法访问父类的私有方法
        # self.__test()
        # 3.可以访问父类的公有属性
        print(self.num1)
        # 4.可以调用父类的公共方法
        self.test()
        pass


b = B()
b.demo()
# 可以在外部访问父类的公有属性和公有方法
print(b.num1)
b.test()
