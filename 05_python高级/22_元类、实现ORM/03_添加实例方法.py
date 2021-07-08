# 传统的创建类的方法
class Test1:
    num1 = 1
    num2 = 2


class Test11(Test1):
    def print_num1(self):
        print(self.num1)


# 用type创建类
Test2 = type("Test2", (), {"num1": 1, "num2": 2})


def print_num1(self):
    print(self.num1)


Test22 = type("Test22", (Test2,), {"print_num1": print_num1})

test11 = Test11()
test22 = Test22()
print(test11.num1)
print(test22.num1)
test11.print_num1()
test22.print_num1()