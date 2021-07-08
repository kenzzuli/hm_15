class UpperAttrMetaClass(type):
    def __new__(cls, class_name, class_parents, class_attr):
        new_attr = {}
        for key, value in class_attr.items():
            if not key.startswith("__"):
                new_attr[key.upper()] = value
        # 两种写法都行
        # 这是复用父类的方法
        return type.__new__(cls, class_name, class_parents, class_attr)
        # 这是完全重新创建类对象
        # return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=UpperAttrMetaClass):
    bar = "bip"


f = Foo()
print(hasattr(f, "bar"))
print(hasattr(f, "BAR"))
# False
# True
