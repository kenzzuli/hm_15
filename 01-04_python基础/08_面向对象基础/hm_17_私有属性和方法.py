class Woman:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __secret(self):
        print("%s的年龄为%d" % (self.name, self.__age))

    # 类中的其他方法可以访问私用属性，调用私有方法
    def show_age(self):
        # 访问私有属性
        print(self.__age)
        # 调用私有方法
        self.__secret()


xm = Woman("小美", 20)

# 无法在外部访问私有属性
# print(xm.__age)
# 无法在外部调用私有方法
# xm.__secret()
xm.show_age()

# 强制访问私有属性和方法，不推荐
# 在私有属性或方法前加上_类名
print(xm._Woman__age)
xm._Woman__secret()