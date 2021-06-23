from timeit import Timer


# 创建列表时间比较
def test1():
    l = []
    for i in range(10000):
        l.append(i)


def test2():
    l = []
    for i in range(10000):
        l = l + [i]


def test6():
    l = []
    for i in range(10000):
        l += [i]


def test3():
    l = [i for i in range(10000)]


def test4():
    l = list(range(10000))


def test5():
    l = []
    for i in range(10000):
        l.extend([i])


timer1 = Timer("test1()", "from __main__ import test1", )
print("append:", timer1.timeit(1000))
timer2 = Timer("test2()", "from __main__ import test2", )
print("+:", timer2.timeit(1000))
timer6 = Timer("test6()", "from __main__ import test6", )
print("+=:", timer6.timeit(1000))
timer3 = Timer("test3()", "from __main__ import test3", )
print("comprehension:", timer3.timeit(1000))
timer4 = Timer("test4()", "from __main__ import test4", )
print("convert:", timer4.timeit(1000))
timer5 = Timer("test5()", "from __main__ import test5", )
print("extend:", timer5.timeit(1000))
# append: 0.5861201119842008
# +: 125.56074387201807
# +=: 0.7242117549758404
# comprehension: 0.31802926800446585
# convert: 0.15147875697584823
# extend: 0.9603683479945175
