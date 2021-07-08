name_list = ["Zhouyan", "Xiaowen", "Simeng", "Guojie", "Zhouyan"]

# len函数可以统计列表中的元素个数
list_len = len(name_list)
print("列表中有%d个元素" % list_len)

# .count方法可以统计列表中某一元素出现的次数
count = name_list.count("Zhouyan")
print("Zhouyan在列表中出现了%d次" % count)

print(name_list)
# .remove方法从列表中删去某一元素的首次出现，如果该元素不存在，会报错
name_list.remove("Zhouyan")

print(name_list)