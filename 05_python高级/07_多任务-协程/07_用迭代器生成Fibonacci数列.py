class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.index = 0
        self.num1 = 0
        self.num2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.n:
            item = self.num1
            self.index += 1
            # 只有python才有这种骚操作
            # self.num1 = self.num2
            # self.num2 = item + self.num2
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return item
        else:
            self.index = 0  # 全部重置
            self.num1 = 0
            self.num2 = 1
            raise StopIteration


f = Fibonacci(10)
for i in f:
    print(i, end="\t")
print()
for i in f:
    print(i, end="\t")
print()

# 0	1	1	2	3	5	8	13	21	34
# 0	1	1	2	3	5	8	13	21	34

# 不要把list简单理解为类型转换，其原理是
# 1.先生成一个空列表
# 2.然后调用可迭代对象的__iter__方法获取迭代器（一般就是自身）
# 3.再调用迭代器的__next__方法获取值，将值放入列表中
# 4.重复3，直到迭代完成
f_list = list(f)
f_tuple = tuple(f)
print(f_list)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(f_tuple)
# (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)
