# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyspiderPipeline:
    def process_item(self, item, spider):
        print(spider)  # <ItcastSpider 'itcast' at 0x7fc6f0491ef0>
        item["hello"] = "world"
        # print(item)
        return item


# pipeline必须有return，不然后面的pipeline接收的数据就是None

# 再加一个管道
class MyspiderPipeline1:
    def process_item(self, item, spider):
        print(item)
        return item
