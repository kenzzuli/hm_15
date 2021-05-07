class Money(object):
    def __init__(self):
        self.__money = 0

    # 使用装饰器对money装饰
    # 获取money时，调用该方法
    @property
    def money(self):
        return self.__money

    # 设置money时，调用该方法
    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("money必须是int类型，设置失败")


m = Money()
m.money = 100
print(m.money)
m.money = "abc"
# 100
# money必须是int类型，设置失败
