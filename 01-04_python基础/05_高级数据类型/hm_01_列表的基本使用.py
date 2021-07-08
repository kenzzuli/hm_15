name_list = ["zhangsan", "lisi", "wangwu"]

# 1.取值和取索引
# 根据索引取值
print(name_list[0])

# 根据值取索引
print(name_list.index("lisi"))


# 2.修改
# 修改指定索引的值
name_list[1] = "Peter"


# 3.增加
# 向列表的末尾追加值
name_list.append("Guojie")

# 向列表的指定索引处插入值
name_list.insert(0, "Zhouyan")
name_list.insert(1, 2)

# 将另一个列表的全部值追加到当前列表
girls = ["Xiaowen", "Simeng", "Yanyan"]
name_list.extend(girls)


# 4.删除
# 删去第一个出现的指定值
name_list.remove(2)
name_list.remove("wangwu")

# 删去末尾的值（弹栈）
print(name_list.pop())

# 删去指定索引的值
print(name_list.pop(0))
del name_list[2]

# 清空列表
name_list.clear()

print(name_list)
