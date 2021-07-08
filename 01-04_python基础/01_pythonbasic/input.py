'''
**需求**

* **收银员输入** 苹果的价格，单位：**元／斤**
* **收银员输入** 用户购买苹果的重量，单位：**斤**
* 计算并且 **输出** 付款金额
'''
price = float(input('please input price:'))
weight = float(input('please input weight:'))
total: float = price * weight
print(total)
print(
    'the price of apple is %f, the weight of apple is %f, and the total money is %.02f' % (price, weight, total))
print("the price is %.2f" % price)
print("the weight is %.2f" % weight)
print("the sum is %.2f" % total)
print("price: %.1f, weight: %.1f, sum: %.1f" % (price, weight, total))
print("int %6d" % price)
