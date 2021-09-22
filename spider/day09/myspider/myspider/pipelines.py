# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging

logger = logging.getLogger(__name__)


# 三个管道分别处理来自三个不同网站的数据
class MyspiderPipeline:
    def process_item(self, item, spider):  # 这里的spider是spider类的实例
        if spider.name == "itcast":
            logger.warning("来自pipeline的warning")
            pass
        return item


class MyspiderPipeline1:
    def process_item(self, item, spider):
        if spider.name == "itcast1":
            pass
        return item


class MyspiderPipeline2:
    def process_item(self, item, spider):
        if spider.name == "itcast2":
            pass
        return item
