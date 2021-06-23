from timeit import Timer


def test1():
    l = []
    for i in range(10000):
        l.append(i)


def test2():
    l = []
    for i in range(10000):
        l.insert(0, i)


timer1 = Timer("test1()", "from __main__ import test1")
print("append: ", timer1.timeit(1000))
timer2 = Timer("test2()", "from __main__ import test2")
print("insert(0): ", timer2.timeit(1000))
# append:  0.5960553759941831
# insert(0):  15.280610996007454
