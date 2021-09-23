class Furniture:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s的面积为%.2f." % (self.name, self.area)


class House:
    # 这里的furniture_list 默认参数不能给[]，列表是可变类型，多次调用共享同一个默认参数。
    # 错误参见 hm_12_默认参数为可变数据类型，原理参见 hm_12_测试.py
    def __init__(self, house_type, area, furniture_list=None):
        self.house_type = house_type
        self.area = area
        self.free_area = area

        if furniture_list is None:
            self.furniture_list = []
        else:
            self.furniture_list = furniture_list
            # 如果房子一开始有家具 去掉相应的面积
            for item in self.furniture_list:
                self.free_area -= item.area

    def __str__(self):
        # 只要打印House对象，就会调用__str__方法

        # 真正的输出开始
        print("_" * 50)
        # python能够自动将一对小括号内的代码连接在一起
        print("户型: %s \n总面积: %.2f\n"
              "空余面积: %.2f\n家具列表: ["
              % (self.house_type, self.area,
                 self.free_area), end="")
        if len(self.furniture_list) > 0:
            for item in self.furniture_list:
                print(item.name, end=", ")
            # 为了模仿列表输出，用[]把遍历的家具的名称包起来
            # 这里的\b表示退格，是为了消去最后多余的逗号空格,
            print("\b\b]")
        else:
            # 如果家具列表内没有元素，就不用退格
            print("]")
        print("_" * 50)
        # 真正的输出结束

        # __str__方法要求返回字符串，这里就返回一个空字符串
        return ""

    def add_furniture(self, furniture):
        # 先判断，剩余面积是否大于家具面积
        if self.free_area >= furniture.area:
            self.furniture_list.append(furniture)
            self.free_area -= furniture.area
            print("买了%s，它占用面积为%.2f" % (furniture.name, furniture.area))
        else:
            print("%s的剩余面积是%.2f，而%s的面积是%.2f，放不下了!"
                  % (self.house_type, self.free_area, furniture.name, furniture.area))

    def del_furniture(self, furniture):
        # 先判断，要删去的家具是否在家具列表中
        if furniture in self.furniture_list:
            self.furniture_list.remove(furniture)
            self.free_area += furniture.area
            print("扔了%s，释放面积为%.2f" % (furniture.name, furniture.area))
        else:
            print("%s里没有%s!" % (self.house_type, furniture.name))


# 创建家具对象
bed = Furniture("床", 4)
chest = Furniture("衣柜", 2)
table = Furniture("桌子", 1.5)
print(bed)
print(chest)
print(table)

# 创建房子对象
house1 = House("公寓", 120)
print(house1)

# 添加家具
house1.add_furniture(bed)
house1.add_furniture(chest)
house1.add_furniture(table)
# 一个房子里有多个同款家具，这里是有两个桌子
house1.add_furniture(table)
print(house1)

# 删除家具
house1.del_furniture(table)
print(house1)

# 删去一个不存在的家具
house1.del_furniture(table)
print(house1)

# 创建一个有家具的旧房子
house2 = House("旧房子", 200, [bed, table])
print(house2)

# 创建一个小房子
house3 = House("小房子", 6)
print(house3)
# 给小房子添加家具，房间剩余面积小于家具面积时会提示
house3.add_furniture(table)
house3.add_furniture(chest)
house3.add_furniture(bed)
print(house3)
