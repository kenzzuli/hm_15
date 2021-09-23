import pygame

# 游戏的初始化
pygame.init()
# 创建游戏窗口 480*700 返回屏幕对象
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 绘制英雄的飞机图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()


event = pygame.event.poll()

# 游戏循环 -->意味着游戏的正式开始
while True:
    pass


