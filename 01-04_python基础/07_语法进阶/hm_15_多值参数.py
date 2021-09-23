def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1)
demo(1, 2)
# 注意，字典的key不能加引号
demo(1, 2, name="xiaoming")
demo(1, 2, 3, 4, 5, name="xiaoming", age=18, gender=True)
