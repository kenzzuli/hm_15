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


# 创建枪对象
ak47 = Gun("AK47")
ak47.add_bullet(10)
ak47.shoot()
print(ak47)
