class Pager(object):
    def __init__(self, page, num_per_page):
        self.page = page  # 第几页
        self.num_per_page = num_per_page  # 每页多少商品

    @property
    def start(self):  # 起始编号
        return (self.page - 1) * self.num_per_page

    @property
    def end(self):  # 结束编号
        return self.page * self.num_per_page


p1 = Pager(1, 20)
print(p1.start)  # 0
print(p1.end)  # 20
