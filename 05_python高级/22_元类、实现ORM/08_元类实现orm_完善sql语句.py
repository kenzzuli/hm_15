class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 储存实例属性和数据库字段的映射关系 u.uid <--> 数据库中的uid字段
        mappings = dict()
        # 判断是否需要保存
        for k, v in attrs.items():
            # 判断是否是元组的实例对象
            if isinstance(v, tuple):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # 从attrs中删除这些已经在mapping字典中存储的属性
        for k in mappings.keys():
            attrs.pop(k)

        # 将mapping字典和类名保存在attrs中
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致

        # 通过父类名调用父类被重写的方法
        return type.__new__(cls, name, bases, attrs)


class User(metaclass=ModelMetaclass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")

    # 当指定元类之后，以上的类属性将不在类中，而是在__mappings__属性对应的字典中存储
    # 以上User类中有
    # __mappings__ = {
    #     "uid": ('uid', "int unsigned")
    #     "name": ('username', "varchar(30)")
    #     "email": ('email', "varchar(30)")
    #     "password": ('password', "varchar(30)")
    # }
    # __table__ = "User"
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            #  setattr(x, 'y', v) is equivalent to ``x.y = v''
            setattr(self, name, value)
        # 初始化后，self指向的实例对象拥有如下属性
        # {'uid': 12345, 'name': 'Michael', 'email': 'test@orm.org', 'password': 'my-pwd'}

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            # getattr(object, name[, default])
            # Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
            #     When a default argument is given, it is returned when the attribute doesn't
            #     exist; without it, an exception is raised in that case.
            # 获取self指向的实例对象中名为k指向的对象(字符串"uid", "name"等)的属性值
            # 相当于获取self.uid, self.name等
            args.append(getattr(self, k, None))
        # 此时
        # fileds = ["uid", "name", "email", "password"]
        # args = [12345, "Michael", "test@orm.org", "my-pwd")
        # 给字符串加引号
        args_tmp = list()
        for arg in args:
            # 如果是整型
            if isinstance(arg, int):
                args_tmp.append(str(arg))
            # 如果是字符串
            elif isinstance(arg, str):
                args_tmp.append("""'{}'""".format(arg))

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ', '.join(fields), ', '.join(args_tmp))
        print('SQL: %s' % sql)


print(User.__dict__)
u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
print(u.__dict__)
u.save()
# SQL: insert into User (uid, username, email, password) values (12345, 'Michael', 'test@orm.org', 'my-pwd')
# ✅