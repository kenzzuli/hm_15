def demo(*args, **kwargs):
    print(args)
    print(kwargs)


num_tuple = (1, 2, 3)
person_dic = {"name": "xiaoming", "age": 18}
# 会把num_tuple和person_dic一起作为元组传递给args
# demo(num_tuple, person_dic)
# 下方为输出结果
# ((1, 2, 3), {'name': 'xiaoming', 'age': 18})
# {}

print("*" * 50)
# 拆包语法，简化元组/字典变量的传递
demo(*num_tuple, **person_dic)
demo(1, 2, 3, name="xiaoming", age=18)
