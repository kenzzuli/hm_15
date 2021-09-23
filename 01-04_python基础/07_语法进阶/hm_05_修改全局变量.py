# 全局变量
num = 10


def demo_01():
    print("demo01==> %d" % num)


def demo_02():
    # 如果非要在函数内部定义一个与全局变量重名的变量，函数内部会调用内部的变量，而非全局变量
    # 但这样python会提示，与外面作用域的num重名
    # 不允许函数直接修改全局变量的引用————使用赋值语句修改全局变量的值
    # 只是定义了一个局部变量，不会修改到全局变量，只是变量名相同而已
    num = 100
    print("demo02==> %d" % num)


def demo_03():
    # 想要在函数内部修改全局变量的值，要先用global关键字声明
    # global关键字会告诉Python解释器后面的变量是一个全局变量
    # 再使用赋值语句时，就不会创建局部变量
    global num
    num = 11
    print("demo03==>%d" % num)


print("start")
demo_01()
demo_02()
demo_03()
print(num)
print("over")
