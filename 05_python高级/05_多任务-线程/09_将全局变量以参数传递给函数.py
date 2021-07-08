# 测试全局变量是否会被修改
def test(num):
    print(id(num))
    num += 1
    print(id(num))  # id变化


def test2(num_list):
    print(id(num_list))
    num_list += [11]  # 对列表使用+=操作，实质上是调用列表的extend方法！而不是使用相加再赋值的操作！
    print(id(num_list))  # id不变


def test4(num_list):
    print(id(num_list))
    num_list = [66]
    print(id(num_list))  # id变化


def test3(num_list):
    print(id(num_list))
    num_list.append(111)
    print(id(num_list))  # id不变


num = 1
num_list1 = [11, ]
num_list2 = [111, ]
num_list3 = [1111, ]
test(num)
test2(num_list1)
test3(num_list2)
test4(num_list3)

print(num)
print(num_list1)
print(num_list2)
print(num_list3)
# 1
# [11, 11]
# [111, 111]
# [1111]
