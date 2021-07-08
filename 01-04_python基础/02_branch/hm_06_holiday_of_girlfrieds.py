"""
1. 定义 `holiday_name` 字符串变量记录节日名称
2. 如果是 **情人节** 应该 **买玫瑰**／**看电影**
3. 如果是 **平安夜** 应该 **买苹果**／**吃大餐**
4. 如果是 **生日** 应该 **买蛋糕**
5. 其他的日子每天都是节日啊……
"""
holiday_name = input("please input a holiday:")
if holiday_name == "valentine's day":
    print("buy roses")
elif holiday_name == "holloween eve":
    print("buy apple")
elif holiday_name == "birthday":
    print("buy cake")
else:
    print("everyday is a holiday with her")
