# 函数调用 传址而非传值
def test(num):

    print("-" * 50)
    print("%d在内存的地址为%d" % (num, id(num)))

    result = 100
    print("%d在内存的地址为%d" % (result, id(result)))

    return result


a = 1

print("调用函数前a中数据的地址为%d" % id(a))

r = test(a)

print("调用函数后，实参中保存的地址为%d" % id(a))
print("调用函数后，返回值的地址为%d" % id(r))
