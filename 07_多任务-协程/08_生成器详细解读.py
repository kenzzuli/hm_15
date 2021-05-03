# 生成器按步骤详解
def fibonacci(n):
    print("---1---")
    i = 0
    a, b = 0, 1
    while i < n:
        print("---2---")
        yield a  # 函数体中有yield，函数就变成了生成器模板
        print("---3---")
        a, b = b, a + b
        i += 1
        print("---4---")
    return "Done"


# 创建生成器对象
f = fibonacci(10)
# 生成器也是一种迭代器，可以直接使用next方法
ret = next(f)
print(ret)

ret = next(f)
print(ret)

# ---1---  生成器从第一行开始运行
# ---2---  函数运行到yield，挂起，返回值作为ret
# 0        打印ret
# ---3---  函数唤醒，从yield下一行继续运行
# ---4---
# ---2---  函数再次运行到yield，挂起，返回值作为ret
# 1        打印ret
