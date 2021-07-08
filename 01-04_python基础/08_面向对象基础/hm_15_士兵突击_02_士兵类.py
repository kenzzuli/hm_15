class Gun:
    def __init__(self, model, bullet_count=0):
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = bullet_count
        print("[%s]创造完成，子弹数[%d]。" % (self.model, self.bullet_count))

    def __str__(self):
        return "型号：[%s]\n子弹数量：[%d]\n请射击!" % (self.model, self.bullet_count)

    def add_bullet(self, count):
        self.bullet_count += count
        print("[%s]子弹+[%d]!" % (self.model, count))

    def shoot(self):
        # 判断子弹数量
        if self.bullet_count > 0:
            # 发射子弹
            self.bullet_count -= 1
            # 提示发射信息
            print("[%s]发射子弹，剩余[%d]!" % (self.model, self.bullet_count))
        else:
            print("[%s]子弹不足，请装弹！" % self.model)


class Soldier:
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun
        if gun is not None:
            print("士兵[%s]携[%s]前来报道！" % (self.name, self.gun.model))
        else:
            print("士兵[%s]前来报到！" % self.name)

    def __str__(self):
        if self.gun is not None:
            return "士兵[%s]\n武器[%s]\n子弹数[%d]" % (self.name, self.gun.model, self.gun.bullet_count)
        else:
            return "士兵[%s]\n没有武器！" % self.name

    def fire(self):
        # 判断是否有枪
        if self.gun is None:
            print("你还没有枪！")
            return
        else:
            # 喊一声口号
            print("老子今天突突了你们！")
            # 装填子弹
            self.gun.add_bullet(50)
            # 射击
            self.gun.shoot()


# 创建枪对象
ak47 = Gun("AK47")
ak47.add_bullet(10)
ak47.shoot()
print(ak47)

xsd = Soldier("许三多")
xsd.fire()
canon = Gun("意大利炮")
xsd.gun = canon
xsd.fire()

gatling = Gun("加特林")
ll = Soldier("刘磊", gatling)
ll.fire()
