class A:
    def __init__(self):
        self.num1 = 1
        self.__num2 = 2

    def __test(self):
        print("A类私有方法")
        print(self.__num2)

    def test(self):
        print("A类公共方法")
        print(self.__num2)


class B(A):
    def demo(self):
        # 1.无法访问父类的私有属性
        # print(self.__num2)
        # 2.无法访问父类的私有方法
        # self.__test()
        pass


b = B()
b.demo()
