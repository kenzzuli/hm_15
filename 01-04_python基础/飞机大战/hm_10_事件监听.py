import pygame

# 游戏的初始化
pygame.init()
# 创建游戏窗口 480*700 返回屏幕对象
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 创建英雄矩形 记录英雄的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏循环 -->意味着游戏的正式开始
while True:
    # 设置屏幕刷新帧率
    clock.tick(60)

    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
    # 修改英雄位置
    hero_rect.y -= 1
    if hero_rect.bottom <= 0:
        hero_rect.y = screen.get_height()

    # 重新绘制所有图像
    # 如果不再次绘制背景，会产生飞机的残影效果
    # 因为这是同一个屏幕对象，screen最后产生的效果是所有图像的叠加
    # 再次绘制背景就是要把以前的图像全部遮盖住
    screen.blit(bg, (0, 0))
    # blit方法的第二个参数既可以是一个矩形，也可以是一个坐标元组
    screen.blit(hero, hero_rect)
    # screen.blit(hero, (hero_rect.x, hero_rect.y))
    # 更新屏幕
    pygame.display.update()
