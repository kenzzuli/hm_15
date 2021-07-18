# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class BookPipeline:
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))  # 插入前将item转成dict
        return item

    def open_spider(self, spider):  # 实例化mongodb
        client = MongoClient(host=spider.setting.get("MONGO_HOST"),
                             port=spider.setting.get("MONGO_PORT"))
        self.collection = client[spider.setting.get("MONGO_DB")][spider.setting.get("MONGO_COLLECTION")]
