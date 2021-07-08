def test1(a, b, *args, **kwargs):
    # 形参中的*args和**kwargs表示函数可以接收不定长参数，
    # 多余的普通参数会放到args元组中，多余的关键字参数会放到kwargs字典中
    print(a)  # 11
    print(b)  # 22
    print(args)  # (33, 44, 55)
    print(kwargs)  # {'name': 'ken', 'age': 10}
    # 实参中的*args和**kwargs表示对元组和字典解包
    # 把元组变成多个普通参数，把字典变成多个关键字参数
    test2(a, b, args, kwargs)  # 相当于test2(11, 22, (33, 44, 55), {'name': 'ken', 'age': 10})
    test2(a, b, *args, kwargs)  # 相当于test2(11, 22, 33, 44, 55, {'name': 'ken', 'age': 10})
    test2(a, b, *args, **kwargs)  # 相当于test2(11, 22, 33, 44, 55, name="ken", age=10)


def test2(a, b, *args, **kwargs):
    print("-" * 30)
    print(a)
    print(b)
    print(args)
    print(kwargs)


test1(11, 22, 33, 44, 55, name="ken", age=10)


