class Tool(object):
    # 定义类属性
    count = 0

    # 定义类方法
    @classmethod
    def show_tool_count(cls):
        # 在类方法内部访问类属性，或调用其他类方法
        print(cls.count)
        cls.show_again()

    # 再定义一个类方法
    @classmethod
    def show_again(cls):
        print(cls.count)

    # 定义实例方法init，用来初始化实例属性
    def __init__(self, name):
        self.name = name

        # 每创建一个工具实例，类属性count+1
        Tool.count += 1


# 创建工具类的实例
axe = Tool("斧头")
hammer = Tool("锤子")
scissor = Tool("剪刀")

# 通过类名.类方法() 来调用类方法
Tool.show_tool_count()
