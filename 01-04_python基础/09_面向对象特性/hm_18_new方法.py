class MusicPlayer(object):

    # 重写__new__方法 实际上就是对父类的__new__方法进行扩展
    def __new__(cls, *args, **kwargs):
        # 1.创建对象时，new方法会被自动调用
        print("1.分配内存空间，并返回实例的引用")
        # 2.为对象分配空间
        # 依然是调用父类的__new__方法
        instance = super().__new__(cls)
        # 3.返回对象的引用
        return instance

        # 上面的两行代码可以整合为下面一行
        # return super().__new__(cls)

    def __init__(self):
        print("2.接收到实例的引用，初始化该实例的属性")


player = MusicPlayer()
print(player)
