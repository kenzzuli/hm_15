class A(object):
    def get_size(self):
        return 100

    def set_size(self, value):
        print("set size to", value)

    def del_size(self):
        print("delete size")

    size = property(get_size, set_size, del_size, "关于size的各种操作")


a = A()
print(a.size)  # 获取
a.size = 200  # 修改
del a.size  # 删除
print(A.size.__doc__)  # 只能是类名.属性.__doc__
# print(a.size.__doc__)  不能是对象.属性.__doc__

# 100
# set size to 200
# delete size
# 关于size的各种操作
