# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

client = MongoClient()
collection = client["python"]["baidu"]


class TencentPipeline:
    def process_item(self, item, spider):
        collection.insert_one(item)
        return item
