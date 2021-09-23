print("程序开始")

# 根据单步调试，程序运行从上到下，运行到类定义时，显然是进入运行的，并不是直接跳过
class Tool(object):
    # 使用赋值语句定义类属性
    count = 0

    # __init__实例方法，用于初始化实例属性
    def __init__(self, name):
        # 为了验证属性的获取机制
        self.count = 100
        self.name = name

        # 每生产一个实例对象，类属性count就加一
        Tool.count += 1

    # demo实例方法，用于对实例属性进行一系列加工
    def demo(self):
        print(self.name)


# 创造实例对象
axe = Tool("斧头")
saw = Tool("电锯")
hammer = Tool("锤子")
# 访问类属性
print(Tool.count)
# 属性的获取机制，现在实例中查找是否有该属性（实例属性）
# 如果找不到就向上在类中查找是否有该属性(类属性），有则返回，无则报错
print(axe.count)
