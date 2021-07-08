info_tuple = ("zhangsan", 20, 1.8, "lisi", 20, 1.88)

print(info_tuple)


# 取值和取索引
print(info_tuple[0])
print(info_tuple.index(1.80))

# 计数
# 统计某一元素在元组中出现的次数
print(info_tuple.count(20))
# 统计元组中总的元素的个数
print(len(info_tuple))
