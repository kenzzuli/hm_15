# 需求：要判断 某一个字典中 是否存在 指定的 值
#
# * 如果 **存在**，提示并且退出循环
# * 如果 **不存在**，在 **循环整体结束** 后，希望 **得到一个统一的提示**

students = [{"name": "Peter",
             "age": 18,
             "sex": True,
             "height": 1.85},
            {"name": "Ken",
             "age": 22,
             "sex": True,
             "height": 1.99},
            {"name": "Karen",
             "age": 19,
             "sex": False,
             "height": 1.7}]
find_name = ""
# 遍历当前的字典中姓名是否为find_name
for stu in students:
    if stu["name"] == find_name:
        print("%s存在" % find_name)
        # 如果已经找到，直接退出循环，就不需要对后续数据进行比较
        break
else:
    print("%s不存在" % find_name)

print("循环结束")