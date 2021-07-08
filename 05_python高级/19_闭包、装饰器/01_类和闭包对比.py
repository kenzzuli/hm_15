# 类和闭包的对比：
# 使用闭包更节省内存空间，但是开发大程序时，闭包用途不大
class Line(object):
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print(self.k * x + self.b)


line1 = Line(1, 2)
line1(0)
line1(1)
line1(2)
line2 = Line(11, 22)
line2(0)
line2(1)
line2(2)
print("-" * 50)


def line(k, b):
    def compute_y(x):
        print(k * x + b)

    return compute_y


line_1 = line(1, 2)  # 执行line函数，kb为参数，返回compute_y，它是指向函数的变量，这样line_1也是指向函数的变量
# compute_y指向的函数仅包含一句print代码
line_1(0)  # 相当于调用compute_y指向的函数，并传入x，此时compute_y指向的函数中没有kb，会从上一层中寻找kb，然后得到kx+b并打印
line_1(1)
line_1(2)
line_2 = line(11, 22)
line_2(0)
line_2(1)
line_2(2)