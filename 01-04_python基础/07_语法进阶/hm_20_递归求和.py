# 计算 1 + 2 + ... num 的结果
def sum_numbers(num):
    # sum_numbers的作用就是计算前num个数之和
    # 递归出口
    if num == 1:
        return 1
    else:
        # 要计算前num个数之和 只需让num加上前num-1个数之和
        return num + sum_numbers(num - 1)


print(sum_numbers(100))


# 计算n!
def multiply(num):
    if num == 1:
        return 1
    else:
        return num * multiply(num - 1)


print(multiply(5))
