# 1. 定义字符串变量 `name`，输出 **我的名字叫 小明，请多多关照！**
name = "Peter"
print("my name is %s, nice to see you!" % name)

# 2. 定义整数变量 `student_no`，输出 **我的学号是 000001**
stu_num = 1000
print("my student num is %06d." % stu_num)

# 3. 定义小数 `price`、`weight`、`money`，输出 **苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元**
price = 9.0
weight = 5.0
money = price * weight
print("the price is %.2f, the weight is %.2f, and the cost is %.2f." % (price, weight, money))

# 4. 定义一个小数 `scale`，输出 **数据比例是 10.00%**
scale = 0.1
print("the scale is %.2f%%" % (scale * 100))

# end of program
print("*"*100)
