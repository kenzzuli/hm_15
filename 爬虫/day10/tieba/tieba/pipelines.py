# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from requests.utils import unquote
from pymongo import MongoClient
import re


class TiebaPipeline:
    def process_item(self, item, spider):
        # 进一步提取图片url
        if item['img_url_list']:
            item['img_url_list'] = [re.search(r"&src=(.*)", unquote(i)).group(1) for i in item['img_url_list']]
        # 存入数据库
        self.collection.insert_one(dict(item))  # 插入前将item转成dict
        print(item)
        print("*" * 50)
        return item

    def open_spider(self, spider):  # 爬虫启动时会调用该函数
        # 实例化mongo客户端
        client = MongoClient(host=spider.settings.get("MONGO_HOST"),
                             port=spider.settings.get("MONGO_PORT"))
        # 获取collection
        self.collection = client[spider.settings.get("MONGO_DB")][spider.settings.get("MONGO_COLLECTION")]
