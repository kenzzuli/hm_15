name_list = ["zhangsan", "lisi", "wangwu"]

# del 也能删去列表中的元素
# 在日常开发中，要从列表中删除值，建议使用列表自带的方法，不用del关键字
del name_list[1]

# del 关键字本质上是用来将一个变量从内存中删除的
name = "peter"
del name
# 如果使用del关键字将变量删去 后续代码就不能使用该变量
# NameError: name 'name' is not defined
print(name)

print(name_list)
