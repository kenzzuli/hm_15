import random

epoch = 10000000000000000
hit = 0
i = 1
while i <= epoch:
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <= 1:
        hit += 1
    pi = (4.0 * hit / i)
    print("迭代%d次，pi的值为%.100f" % (i, pi))
    i += 1
