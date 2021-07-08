class Tool(object):
    # 使用赋值语句定义类属性
    count = 0

    # __init__实例方法，用于初始化实例属性
    def __init__(self, name):
        # 实例属性
        # self.count = 100
        self.name = name

        # 每生产一个实例，类属性count就加一
        Tool.count += 1

    # demo实例方法，用于对实例属性进行一系列加工
    def demo(self):
        print(self.name)


# 创造实例
axe = Tool("斧头")
saw = Tool("电锯")
hammer = Tool("锤子")
# 访问类属性
print(Tool.count)

# 不推荐通过实例名访问类属性！！！
# 属性的获取机制，现在实例中查找是否有该属性（实例属性）
# 如果找不到就向上在类中查找是否有该属性(类属性），有则返回，无则报错
print(axe.count)

# 如果使用赋值语句 实例.类属性 = 值 ，只会给实例增加一个与类属性同名的实例属性，而不会修改类属性的值
axe.count = 100
print(axe.count)
print(Tool.count)

# 如果使用赋值语句  类.类属性 = 值，可以修改类属性的值
Tool.count = 999
print(Tool.count)