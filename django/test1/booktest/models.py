from django.db import models


# 设计和表对应的类，即模型类
# Create your models here.

class BookInfo(models.Model):
    """图书类"""
    # 图书标题，CharField说明是字符串，max_length指定字符串的最大长度
    btitle = models.CharField(max_length=20)
    # 图书出版日期，DateField说明是日期类型
    bpub_date = models.DateField()

    def __str__(self):
        # 返回书名
        return self.btitle


class HeroInfo(models.Model):
    """英雄类"""
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别，布尔类型，default指定默认值，False代表男生
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性，建立图书类和英雄类之间的一对多关系
    # 关系属性对应的表的字段名格式： 关系属性名_id，这里是hbook_id
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        # 返回英雄名
        return self.hname
