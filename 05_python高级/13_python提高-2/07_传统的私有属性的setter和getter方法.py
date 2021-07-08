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


m = Money()
print(m.get_money())
m.set_money(100)
m.set_money("abc")

# 0
# money必须是int类型，设置失败
