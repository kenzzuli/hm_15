# 传统的创建类的方法
class Test1:
    num1 = 1
    num2 = 2


class Test11(Test1):
    pass


# 用type创建类
Test2 = type("Test2", (), {"num1": 1, "num2": 2})
Test22 = type("Test22", (Test2,), {})

test11 = Test11()
test22 = Test22()
print(test11.num1)
print(test22.num1)
