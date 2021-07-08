from hm_11_摆放家具_01_家具类 import Furniture


class House:
    # 默认参数仅计算一次，若默认参数为列表、字典、大多数类的实例（对象）等可变数据类型，将产生很大不同
    # furniture_list将累加传递给它的参数，并在随后的调用中使用。
    def __init__(self, house_type, area, furniture_list=[]):
        self.house_type = house_type
        self.area = area
        self.free_area = area
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

# create House object
# 首次调用， furniture_list的参数为[]
house1 = House("apartment", 120)
print(house1)
print("*" * 50)

# 添加家具后，furniture_list的参数为[bed]
house1.add_furniture(bed)
# 再次添加家具，furniture_list的参数为[bed, chest]
house1.add_furniture(chest)

# 创建新的对象时，此时使用的furniture_list 仍然是上面的[bed, chest]，而不是[]
# 这与我们的需求不一致
house4 = House("mansion", 500)
print(house4)
