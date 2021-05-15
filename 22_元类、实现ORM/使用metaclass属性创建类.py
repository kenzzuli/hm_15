class UpperAttrMetaClass(type):
    def __new__(cls, class_name, class_parents, class_attr):
        new_attr = {}
        for key, value in class_attr.items():
            if not key.startswith("__"):
                new_attr[key.upper()] = value

        return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=UpperAttrMetaClass):
    bar = "bip"


f = Foo()
print(hasattr(f, "bar"))
print(hasattr(f, "BAR"))
# False
# True