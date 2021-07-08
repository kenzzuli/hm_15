num = 1
nums = [11, 22]
nums2 = [111, 222]
nums3 = [1111, 2222]


def test1():
    global num
    num += 1


def test2():
    nums.append(33)


def test3():
    # nums2.append(333)
    # print(nums2)
    nums2 += [333]


def test4():
    global nums3
    nums3 += [3333]


print(num)
print(nums)
# print(nums2)
print(nums3)
test1()
test2()
# test3()
test4()
print(num)
print(nums)
# print(nums2)
print(nums3)

# 1
# [11, 22]
# [1111, 2222]
# 2
# [11, 22, 33]
# [1111, 2222, 3333]