from django.db import models


# Create your models here.
class BookInfoManager(models.Manager):
    """图书模型管理器类"""

    # 1.改变查询的结果集
    def all(self):
        # 1.调用父类的all方法,获取所有数据
        books = super().all()
        # 2.对数据进行过滤
        books = books.filter(isDelete=False)
        # 3.返回
        return books

    # 2.封装函数，操作模型类对应的数据表（增删改查）
    def create_book(self, btitle, bpub_date):
        # 1.创建图书对象
        book = self.model()
        book.btitle = btitle
        book.bpub_date = bpub_date
        # 2.保存进数据库
        book.save()
        # 3.返回图书对象
        return book


class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称
    # btitle = models.CharField(max_length=30)
    btitle = models.CharField(max_length=30, unique=True, db_index=True, db_column='title')
    # 图书价格 总位数为10，小数位数为2
    # bprice = models.DecimalField(default=9.88, max_digits=10, decimal_places=2)
    # 出版日期
    bpub_date = models.DateField()
    # 阅读量，默认为0
    bread = models.IntegerField(default=0)
    # 评论量，默认为0
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)
    # book = models.Manager()  # 自定义一个Manager类对象
    objects = BookInfoManager()  # 自定义一个BookInfoManager类的对象

    # @classmethod
    # def create_book(cls, btitle, bpub_date):
    #     # 1.创建一个图书对象
    #     obj = cls()
    #     obj.btitle = btitle
    #     obj.bpub_date = bpub_date
    #     # 2.保存进数据库
    #     obj.save()
    #     # 3.返回obj
    #     return obj

    # 定义元选项
    class Meta:
        db_table = 'bookinfo'  # 指定BookInfo生成的数据表名为bookinfo


class HeroInfo(models.Model):
    """英雄模型类"""
    # 英雄名称
    hname = models.CharField(max_length=20)
    # 英雄性别 默认为男性
    hgender = models.BooleanField(default=False)
    # 英雄备注
    hcomment = models.CharField(max_length=100, null=True, blank=False)
    # 所属图书
    hbook = models.ForeignKey('BookInfo')
    # 删除标记
    isDelete = models.BooleanField(default=False)


class AreaInfo(models.Model):
    """地区模型类"""
    # 地区名称
    atitle = models.CharField(max_length=20)
    # 关系属性，代表当前地区的父级地区的id，允许为空，后台也允许为空
    aParent = models.ForeignKey('self', null=True, blank=True)
