# 传统的创建类的方法
class Test1:
    num1 = 1
    num2 = 2


class Test11(Test1):
    def print_num1(self):
        print(self.num1)

    @classmethod
    def cls_func(cls):
        print(cls.__class__)

    @staticmethod
    def stt_func():
        print("静态方法")


# 用type创建类
Test2 = type("Test2", (), {"num1": 1, "num2": 2})


def print_num1(self):
    print(self.num1)


@classmethod
def cls_func(cls):
    print(cls.__class__)


@staticmethod
def stt_func():
    print("静态方法")


Test22 = type("Test22", (Test2,), {"print_num1": print_num1, "cls_func": cls_func, "stt_func": stt_func})

test11 = Test11()
test22 = Test22()
# 调用类属性
print(test11.num1)
print(test22.num1)
# 调用实例方法
test11.print_num1()
test22.print_num1()
# 调用类方法
test11.cls_func()
test22.cls_func()
# 调用静态方法
test11.stt_func()
test22.stt_func()
# 1
# 1
# 1
# 1
# <class 'type'>
# <class 'type'>
# 静态方法
# 静态方法
