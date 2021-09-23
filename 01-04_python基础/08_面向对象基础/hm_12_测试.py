# 默认参数仅计算一次，若默认参数为列表、字典、大多数类的实例等可变对象，将产生巨大差异！
# 下面的函数将会累加曾经传给它的参数，并传给下一次调用。
def f(a, L=[]):
    L.append(a)
    return L


# 此时打印[1]
print(f(1))
# 打印[1, 2]
print(f(2))
# 打印[1, 2, 3]
print(f(3))


# 若不想在随后的调用中共享这些默认参数，可以这样修改函数：

def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# 这样每次调用，默认参数互不影响
print(f1(1))
print(f1(2))
print(f1(3))
