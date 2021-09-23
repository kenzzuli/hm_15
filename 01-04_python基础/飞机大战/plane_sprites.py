import random
import pygame

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 屏幕刷新的帧率
FRAME_RATE = 60
# 创建敌机的 计时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 敌机出现的时间间隔
ENEMY_TIME_INTERVAL = 1000
# 发射子弹的 计时器时间常量
FIRE_BULLET_EVENT = pygame.USEREVENT + 1
# 发射子弹的时间间隔
FIRE_TIME_INTERVAL = 500


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    # 这里的形参image_name就是普通的图像的名称，不是图像对象
    def __init__(self, image_name, speed=1):
        super().__init__()
        # 通过加载，返回图像对象
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵类，产生背景连续移动效果"""

    def __init__(self, is_alt=False, image_name="./images/background.png", speed=1):
        # 1> 调用父类方法实现精灵的创建（image, rect, speed)
        super().__init__(image_name, speed)
        # 2> 判断是否是第二张照片
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的方法
        super().update()
        if self.rect.y >= self.rect.height:
            self.rect.y = -self.rect.height


class ENEMY(GameSprite):
    """敌机精灵"""

    def __init__(self, image_name="./images/enemy1.png"):
        # 1> 敌机的随机速度
        speed = random.randint(1, 10)
        super().__init__(image_name, speed)
        # 2> 敌机水平方向的随机位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        # 3> 敌机一点点出现，不突兀
        # self.rect.y = -self.rect.height
        self.rect.bottom = 0

    def __del__(self):
        # 析构函数
        # print("飞出屏幕，%s死了！" % self.rect)
        pass

    def update(self):
        # 1> 调用父类方法，实现敌机在垂直方向的位置变化
        super().update()
        # 2> 如果敌机飞出屏幕，删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # kill方法可以将精灵从所有精灵组中移除，精灵会被自动销毁
            self.kill()


class Hero(GameSprite):
    """英雄飞机"""

    def __init__(self, image_name="./images/me1.png", speed=10):
        # 1> 调用父类的初始化方法，设置英雄的图像和速度
        super().__init__(image_name, speed)
        # 2> 设置英雄的初始位置
        # 英雄水平居中
        # self.rect.x = -0.5*self.rect.width + 0.5* SCREEN_RECT.width
        self.rect.centerx = SCREEN_RECT.centerx
        # 英雄距离底部120像素
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 子弹属性
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.bullets.update()

    def fire(self):
        # 一次发射三颗子弹
        # i = 0
        # while i < 45:
        #     # 创建子弹精灵
        #     bullet = Bullet()
        #     # 设置子弹的位置
        #     bullet.rect.centerx = self.rect.centerx
        #     bullet.rect.top = self.rect.top + i
        #     # 将精灵添加到精灵组
        #     self.bullets.add(bullet)
        #     i += 15
        # 由while循环换成了for循环
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.top = self.rect.top + 20 * i
            self.bullets.add(bullet)

    def move_left(self):
        if self.rect.x > self.speed:
            self.rect.x -= self.speed

    def move_right(self):
        if self.rect.right < SCREEN_RECT.width - self.speed:
            self.rect.x += self.speed

    def move_up(self):
        if self.rect.y > self.speed:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.bottom < SCREEN_RECT.bottom - self.speed:
            self.rect.y += self.speed


class Bullet(GameSprite):
    """子弹"""

    def __init__(self, image_name="./images/bullet1.png", speed=2):
        super().__init__(image_name, speed)

    def update(self):
        self.rect.y -= self.speed
        # 如果飞出屏幕，自动销毁
        if self.rect.bottom <= 0:
            self.kill()
