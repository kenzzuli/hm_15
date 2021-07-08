# 实际开发中使用三种装饰器
class Goods:
    def __init__(self, original_price, discount):
        self.original_price = original_price
        self.discount = discount

    @property
    def real_price(self):
        return self.discount * self.original_price

    @real_price.setter
    def real_price(self, price):
        self.original_price = price / self.discount

    @real_price.deleter
    def real_price(self):
        del self.original_price


g = Goods(100, 0.8)
print(g.real_price)  # 获取 商品实际价格 80.0
g.real_price = 200  # 修改 商品实际价格，顺带会根据折扣更改商品的原始价格
print(g.original_price)  # 250.0
del g.real_price  # 删除 商品实际价格，会删除商品的原始价格
# print(g.original_price)  # AttributeError: 'Goods' object has no attribute 'original_price'
