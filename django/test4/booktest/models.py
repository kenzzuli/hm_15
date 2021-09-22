from django.db import models


# Create your models here.
class BookInfo(models.Model):
    """图书模型类"""
    btitle = models.CharField(max_length=30, db_column='title')
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
