class A:
    def __init__(self):
        self.name = "A"

    def test(self):
        print("A类test")

    def demo(self):
        print("A类demo")


class B:
    def __init__(self):
        self.name = "B"

    def demo(self):
        print("B类demo")

    def test(self):
        print("B类test")


class C(A, B):
    # 多继承可以让子类对象同时拥有多个父类的属性和方法
    pass


c = C()
# 类名.__mro__ 方法解析顺序 确定一个多继承子类的方法和属性的调用顺序
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# 先从 C 找，再从 A 找，再从 B 找，最后从 object （Python所有类的基类）找，如果还找不到就报错。
print(C.__mro__)
c.test()
c.demo()
print(c.name)

