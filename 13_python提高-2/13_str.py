class Test(object):
    def __str__(self):
        return "调用str方法"


test = Test()
# 1.直接打印
print(test)
# 调用str方法
# 2.字符串拼接中
print("对象的描述信息为: %s" % test)
# 对象的描述信息为: 调用str方法
a = [11, 22, 33]
