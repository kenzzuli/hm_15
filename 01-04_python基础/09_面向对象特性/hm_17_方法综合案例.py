class Game(object):
    # 类属性 最高分
    top_score = 0

    # 类方法 显示最高分
    @classmethod
    def show_top_score(cls):
        print(cls.top_score)

    # 实例方法，初始化实例属性
    def __init__(self, player_name):
        self.player_name = player_name

    # 实例方法 开始游戏
    def start_game(self):
        print("%s正沉迷游戏，无法自拔。。。。" % self.player_name)

    # 静态方法 打印帮助信息
    @staticmethod
    def help():
        print("假装这里有一份帮助文档")


# 调用静态方法
Game.help()
# 调用类方法
Game.show_top_score()
# 调用实例方法
game = Game("刘壮壮")
game.start_game()
