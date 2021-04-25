# 测试全局变量是否会被修改
def test(num):
    num += 1


def test2(num_list):
    num_list += [11]


def test3(num_list):
    num_list.append(111)


num = 1
num_list1 = [11, ]
num_list2 = [111, ]
test(num)
test2(num_list1)
test3(num_list2)

print(num)
print(num_list1)
print(num_list2)

# 1
# [11, 11]
# [111, 111]
