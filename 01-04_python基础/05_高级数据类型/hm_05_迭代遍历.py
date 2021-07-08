name_list = ["Zy", "Zxw", "Lsm", "Gj"]
# 使用迭代遍历列表
"""
顺序的从列表中依次获取元素，每一次循环中，元素都将保存在 name 变量中
在循环体内部可以访问到当前循环获取到的元素

for 变量名 in 列表变量：
    语句1
    语句2
"""
for name in name_list:
    print("%s wants to make love to Ken" % name)

i = 0
while i < len(name_list):
    name = name_list[i]
    print("Ken wanna fuck %s" % name)
    i += 1
