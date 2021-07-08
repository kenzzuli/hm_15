class MusicPlayer(object):
    # 定义类属性 记录第一个被创建的实例的引用
    instance = None

    # 重写__new__方法 静态方法
    def __new__(cls, *args, **kwargs):
        # 判断类属性instance是否为None,即是否已经存在实例
        if cls.instance is None:
            # 若实例不存在，则调用父类的__new__方法创建实例并将其引用赋值给类属性instance
            cls.instance = super().__new__(cls)
        # 最后直接返回类属性
        return cls.instance

    def __init__(self):
        print("播放器初始化。。。。")


player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
