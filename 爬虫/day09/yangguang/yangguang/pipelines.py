# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from yangguang.items import YangguangItem
import re


class YangguangPipeline:
    def process_item(self, item, spider):
        print(spider.setting.get("MONGO_HOST"))
        if isinstance(item, YangguangItem):
            # 处理item，去除字符串中的空白字符
            for k, v in item.items():
                if v and isinstance(v, str):
                    item[k] = v.strip()
            # 处理item中的detail
            item["detail"] = self.process_detail(item["detail"])
            print(item)
            print("-" * 50)
            # 在这里可以直接调用在open_spider中实例化的mongodb
            self.collection.insert(dict(item))
        return item

    def process_detail(self, detail):  # 将其中的\r\n换成\n
        return re.sub(r"\r\n", r"\n", detail, flags=re.S)

    def open_spider(self, spider):  # 开启爬虫时执行一次
        spider.hello = "world"
        # 开启爬虫时实例化mongodb
        client = MongoClient()
        self.collection = client["python"]["yangguang"]


    def close_spider(self, spider):  # 关闭爬虫时执行一次
        pass
