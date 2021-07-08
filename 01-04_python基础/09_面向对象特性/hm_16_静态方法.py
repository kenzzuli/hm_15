class Dog(object):
    def __init__(self, name):
        self.name = name

    # 定义静态方法，既不访问类属性或方法，也不访问实例属性或方法
    @staticmethod
    def run():
        print("狗子在跑步。。。。")

    @staticmethod
    def walk():
        print("狗子在散步。。。。")


# 通过 类名.静态方法() 来调用静态方法
Dog.run()
