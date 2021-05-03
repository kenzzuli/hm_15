# 使用异常获取生成器的返回值，即return后的值
def fibonacci(n):
    i = 0
    a, b = 0, 1
    while i < n:
        yield a  # 函数体中有yield，函数就变成了生成器模板
        a, b = b, a + b
        i += 1
    return "Done"


f = fibonacci(10)

while True:
    try:
        ret = next(f)
        print(ret, end="\t")
    except StopIteration as e:
        print()
        print(e.value)  # 打印返回值
        break
# 0	1	1	2	3	5	8	13	21	34
# Done
