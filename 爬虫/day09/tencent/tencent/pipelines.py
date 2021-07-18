# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from tencent.items import TencentItem

client = MongoClient()
collection = client["python"]["baidu"]


class TencentPipeline:
    def process_item(self, item, spider):
        # 这里可以对item的类型进行判断，进而达到不同类型的item经过不同的处理的效果
        if isinstance(item, TencentItem):
            # 这里需要把item转为字典，才能插入mongodb
            collection.insert_one(dict(item))
        return item
