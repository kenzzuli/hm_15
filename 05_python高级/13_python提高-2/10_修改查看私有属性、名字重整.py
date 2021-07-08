class Test(object):
    def __init__(self, name):
        self.__name = name  # 定义私有属性


test = Test("peter")
print(test.__dict__)  # 在创建对象时，私有属性的名字被修改了，这就是名字重整
# {'_Test__name': 'peter'}
print(test._Test__name)  # 加上 _类名 能够访问私有属性
# peter

test.__name = "ken"  # 此时只是纯粹的增加一个属性，不存在公有私有之说
print(test.__dict__)
# {'_Test__name': 'peter', '__name': 'ken'}  # 在字典中可以看到，这是两个不同的变量
print(test.__name)  # 此时__name不是私有属性，只有创建对象时名字重整的才是私有属性
# ken
