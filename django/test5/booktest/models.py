from django.db import models


# Create your models here.
class AreaInfo(models.Model):
    """地区模型类"""
    # 地区名称
    atitle = models.CharField(verbose_name="地区", max_length=20)
    # 自关联属性
    # 使用verbose_name指定该属性对应列的列名
    aParent = models.ForeignKey('self', verbose_name="上级地区", null=True, blank=True)

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle

    # 指定方法对应的列根据哪个字段进行排序
    title.admin_order_field = 'atitle'
    # 指定方法对应的列的名称
    title.short_description = '地区名称'

    def parent(self):
        # 如果没有父级地区，直接返回空字符串
        if self.aParent is None:
            return ""
        # 如果有父级地区，则返回父级地区的atitle
        return self.aParent.atitle

    parent.admin_order_field = 'aParent'
    parent.short_description = '父级地区'


class PicTest(models.Model):
    """上传图片"""
    # 指定上传到MEDIA_ROOT中的哪个文件夹
    goods_pic = models.ImageField(upload_to='booktest')
