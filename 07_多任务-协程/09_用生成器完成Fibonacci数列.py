# 用生成器完成Fibonacci数列
def fibonacci(n):
    i = 0
    a, b = 0, 1
    while i < n:
        yield a  # 函数体中有yield，函数就变成了生成器模板
        a, b = b, a + b
        i += 1
    return "Done"


# 创建生成器对象
f = fibonacci(10)
print(f)
# <generator object fibonacci at 0x7f90ac8c84c0>
for i in f:
    print(i, end="\t")
# 0	1	1	2	3	5	8	13	21	34
print()
# 但是生成器对象无法第二次迭代
for i in f:
    print(i, end="\t")
