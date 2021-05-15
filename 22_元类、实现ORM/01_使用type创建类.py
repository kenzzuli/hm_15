# 传统的创建类的方法
class Test1:
    num1 = 1
    num2 = 2


# 用type创建类
Test2 = type("Test2", (), {"num1": 1, "num2": 2})

test1 = Test1()
test2 = Test2()
print(test1.num1)
print(test2.num1)
