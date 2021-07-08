class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 储存实例属性和数据库字段的映射关系 u.uid <--> 数据库中的uid字段
        mappings = dict()
        # 判断是否需要保存
        for k, v in attrs.items():
            # 判断是否是元组的实例对象
            if isinstance(v, tuple):
                mappings[k] = v

        # 从attrs中删除这些已经在mapping字典中存储的属性
        for k in mappings.keys():
            attrs.pop(k)

        # 将mapping字典和类名保存在attrs中
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致

        # 通过父类名调用父类被重写的方法
        return type.__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))
        # 数据类型检测
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


class User(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")


class Order(Model):
    id = ("id", "int unsigned")
    product_id = ("product_id", "int unsigned")
    quantity = ("quantity", "int unsigned")
    user_name = ("user_name", "varchar(30)")


u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
# SQL: insert into User (uid, username, email, password) values (12345, 'Michael', 'test@orm.org', 'my-pwd')

order = Order(id=1, product_id=10001, quantity=3, user_name="ken")
order.save()
# SQL: insert into Order (id, product_id, quantity, user_name) values (1, 10001, 3, 'ken')
