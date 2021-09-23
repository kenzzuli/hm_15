def sum_number(num):
    print(num)

    # 编写递归函数时，一定要有递归的出口，即函数满足某一条件时，停止递归
    if num == 1:
        return
    # 函数内部调用自己
    sum_number(num - 1)
    print("完成%d" % num)


sum_number(3)
