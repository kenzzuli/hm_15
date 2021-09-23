import pygame

pygame.init()

# 创建游戏窗口 480*700 返回屏幕对象
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 1>加载图像
bg = pygame.image.load("./images/background.png")
# 2>将图像绘制到屏幕的指定位置
screen.blit(bg, (0, 0))
# 3>更新屏幕
pygame.display.update()


event = pygame.event.poll()

# 游戏循环
while True:
    pass
# while True:
#     event = pygame.event.poll()
#     if event.type == pygame.QUIT:
#         pygame.quit()
#         exit()

