import pygame
from plane_sprites import *


# 创建游戏类
class PlaneGame(object):

    # 游戏初始化
    def __init__(self):
        # 1> 设置游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2> 设置游戏时钟
        self.clock = pygame.time.Clock()
        # 3> 创建精灵，精灵组
        self.__create_sprites()
        # 4> 设置定时器事件 创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, ENEMY_TIME_INTERVAL)
        # 5> 设置计时器事件 发射子弹
        pygame.time.set_timer(FIRE_BULLET_EVENT, FIRE_TIME_INTERVAL)

    # 创建精灵，精灵组
    def __create_sprites(self):
        # 1>背景精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        # 2>敌人精灵组
        self.enemy_group = pygame.sprite.Group()
        # 3>英雄精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 开始游戏循环
    def start_game(self):
        print("游戏开始...")
        while True:
            # 1>设置刷新帧率 这个时钟必须放到循环内部，放在循环外部没有效果
            self.clock.tick(FRAME_RATE)
            # 2>事件监听
            self.__event_handler()
            # 3>碰撞检测
            self.__check_collide()
            # 4>更新/绘制精灵
            self.__update_sprites()
            # 5>更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = ENEMY()
                self.enemy_group.add(enemy)
            elif event.type == FIRE_BULLET_EVENT:
                self.hero.fire()
            # 1>这种方式，用户必须抬起按键，再按下按键，才算一次按键事件，操作不够灵活
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #     self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            #     self.hero.move_left()
        # 2>这样按下按键不松，会当成多个事件，操作更加灵活
        # 返回所有按键的元组，若被按下，对应的值为1
        keys_pressed = pygame.key.get_pressed()
        # 获取元组中某一按键的状态，若按下，则为1
        if keys_pressed[pygame.K_SPACE]:
            self.hero.fire()
        if keys_pressed[pygame.K_LEFT]:
            self.hero.move_left()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.move_right()
        if keys_pressed[pygame.K_UP]:
            self.hero.move_up()
        if keys_pressed[pygame.K_DOWN]:
            self.hero.move_down()

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机摧毁精灵
        if len(pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True)) > 0:
            print("英雄牺牲！")
            PlaneGame.__game_over()

    def __update_sprites(self):

        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero.bullets.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
