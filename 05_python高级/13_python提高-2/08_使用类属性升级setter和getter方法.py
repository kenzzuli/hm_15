class Money(object):
    def __init__(self):
        self.__money = 0

    def get_money(self):
        return self.__money

    def set_money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("money必须是int类型，设置失败")

    money = property(get_money, set_money)  # 类属性方法创建property属性


m = Money()
m.money = 100
print(m.money)
m.money = "abc"
# 100
# money必须是int类型，设置失败
