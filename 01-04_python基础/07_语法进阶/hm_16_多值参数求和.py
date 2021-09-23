def sum_numbers(*args):

    num = 0
    for arg in args:
        num += arg
    print(num)


sum_numbers()
sum_numbers(1)
sum_numbers(1, 2)
sum_numbers(1, 2, 3)
sum_numbers(1, 2, 3, 4)
