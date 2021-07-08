# for 循环可以遍历所有非数字型的变量，如 列表 元组 字典 字符串

# 遍历 元组 很少对元组进行遍历，因为元组内的元素的类型通常不相同
info_tuple = ("zhangsan", 18, 1.83)

for item in info_tuple:
    print(item)

# 遍历 字符串
for char in "i love you!":
    print(char)

# 遍历 列表
name_list = ["peter", "ken", "jacky"]
for name in name_list:
    print(name)

# 遍历 字典
dic = {'id': 1, "phone": 1589007505}
print(type(dic))

for key in dic:
    print(dic[key])

