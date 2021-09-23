class MusicPlayer(object):
    # 定义类属性 记录第一个被创建的实例的引用
    instance = None
    # 类属性，记录是否被初始化
    init_flag = False

    # 重写__new__方法 静态方法
    def __new__(cls, *args, **kwargs):
        # 判断类属性instance是否为None,即是否已经存在实例
        if cls.instance is None:
            # 若实例不存在，则调用父类的__new__方法创建实例并将其引用赋值给类属性instance
            cls.instance = super().__new__(cls)
        # 最后直接返回类属性
        return cls.instance

    def __init__(self):
        # 如果被初始化过，则直接返回
        if MusicPlayer.init_flag:
            return
        # 如果没有，初始化，并将类属性init_flag置为True，
        print("播放器初始化。。。。")
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
