# """
# #### 逻辑运算演练
# """
# # 1. 练习1: 定义一个整数变量 `age`，编写代码判断年龄是否正确
# # * 要求人的年龄在 0-120 之间
# age = int(input("please input age:"))
# if 0 <= age <= 120:
#     print("age is valid!")
# else:
#     print("invalid")
#
# # 2. 练习2: 定义两个整数变量 `python_score`、`c_score`，编写代码判断成绩
# # * 要求只要有一门成绩 > 60 分就算合格
# python_score = int(input("python score:"))
# c_score = int(input("c score:"))
# if python_score >60 or c_score > 60:
#     print("pass")
# else:
#     print("fail")

# 3. 练习3: 定义一个布尔型变量 `is_employee`，编写代码判断是否是本公司员工
# # * 如果不是提示不允许入内
# x = int(input("0 for not, 1 for yes:"))
# print("x = " + str(x))
# is_employee = bool(x)
# print("is_employee = " + str(is_employee))
# print("&&&&&&&&&&&")
is_employee = int(input("0 for not, 1 for yes:"))
if is_employee:
    print("welcome back!")
else:
    print("unlogged people!")
if not is_employee:
    print("unlogged people!")
else:
    print("welcome back!")
print("^^^^^^^^^^^^^^")
is_emp = bool(int(input("0 for not, 1 for yes")))
if not is_emp:
    print("fuck off")
else:
    print("come on in")
print("***********")
emp=int(input("0 for not, 1 for yes:"))
print(emp)
if emp:
    print("welcome")
else:
    print("fuck off")
