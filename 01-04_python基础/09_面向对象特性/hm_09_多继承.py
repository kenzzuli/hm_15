class A:
    def test(self):
        print("A类方法")


class B:
    def demo(self):
        print("B类方法")


class C(A, B):
    # 多继承可以让子类对象同时拥有多个父类的属性和方法
    pass


c = C()
c.test()
c.demo()