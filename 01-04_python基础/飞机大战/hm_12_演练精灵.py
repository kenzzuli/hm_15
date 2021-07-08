import pygame
from plane_sprites import *

# 游戏的初始化
pygame.init()
# 创建游戏窗口 480*700 返回屏幕对象
screen = pygame.display.set_mode((480, 700))
# 创建背景图像
bg = pygame.image.load("./images/background.png")

# 创建英雄图像
hero = pygame.image.load("./images/me1.png")
# 创建英雄矩形 记录英雄的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌人
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png", 2)
enemy2.rect.x = 200
# 将敌人放入一个精灵组
enemy_group = pygame.sprite.Group(enemy1, enemy2)

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环 -->意味着游戏的正式开始
while True:
    # 设置屏幕刷新帧率
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():
        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏....")
            pygame.quit()
            exit()
    # 修改英雄位置
    hero_rect.y -= 1
    if hero_rect.bottom <= 0:
        hero_rect.y = screen.get_height()

    # 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    # blit方法的第二个参数既可以是一个矩形，也可以是一个坐标元组
    screen.blit(hero, hero_rect)

    # 更新敌人位置
    enemy_group.update()
    # 绘制敌人
    enemy_group.draw(screen)

    # 更新屏幕 显示到屏幕上
    pygame.display.update()
