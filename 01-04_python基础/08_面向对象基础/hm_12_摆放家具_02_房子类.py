from hm_11_摆放家具_01_家具类 import Furniture


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
        # python能够自动将一对小括号内的代码连接在一起
        return ("house_type: %s \ntotal_area: %.2f\n"
                "free_area: %.2f\nfurniture_list : %s"
                % (self.house_type, self.area,
                   self.free_area, self.furniture_list))

    def add_furniture(self, furniture):
        if self.free_area >= furniture.area:
            self.furniture_list.append(furniture)
            self.free_area -= furniture.area
            print("buy a %s, and it covers an area of %.2f" % (furniture.name, furniture.area))
        else:
            print("the free area of %s is %.2f, while the area of %s is %.2f!"
                  % (self.house_type, self.free_area, furniture.name, furniture.area))

    def del_furniture(self, furniture):
        if furniture in self.furniture_list:
            self.furniture_list.remove(furniture)
            self.free_area += furniture.area
            print("throw away a %s, and it frees an area of %.2f" % (furniture.name, furniture.area))
        else:
            print("%s is not in the house." % furniture.name)


# create Furniture object
bed = Furniture("Ximengsi", 4)
chest = Furniture("Yibang", 2)
table = Furniture("Sanjiu", 1.5)
print(bed)
print(chest)
print(table)

# create House object
house1 = House("apartment", 120)
print(house1)
print("*" * 50)

house2 = House("oldhouse", 200, [bed, table])
print(house2)

print("_" * 50)
house1.add_furniture(bed)
print(house1)
print("*" * 50)

house1.add_furniture(chest)
print(house1)
print("*" * 50)

house1.add_furniture(table)
print(house1)
print("*" * 50)

house1.del_furniture(table)
print(house1)
print("*" * 50)

house1.del_furniture(table)
print(house1)
print("*" * 50)

house3 = House("tinyhouse", 6)
print(house3)
house3.add_furniture(table)
house3.add_furniture(chest)
house3.add_furniture(bed)
