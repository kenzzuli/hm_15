# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from requests.utils import unquote
from pymongo import MongoClient
import re
from tieba.spiders.tieba3 import Tieba3Spider


class TiebaPipeline:
    def process_item(self, item, spider):
        # 在抓取过程中，有时会被重定向到错误页面，https://gsp0.baidu.com/5aAHeD3nKhI2p27j8IqW0jdnxx1xbK/tb/error.html?tc=19428019652428576522081301
        # 此页面内容为空，提取不到数据
        # 确保数据的有效性，如果poster或title为None，直接放弃

        if item['poster'] and item['title']:
            # 进一步处理图片url
            if item['img_url_list']:
                item['img_url_list'] = [unquote(i).split("src=")[-1] for i in item['img_url_list']]

            # 如果item来自爬虫tieba3 还需要处理poster和title
            if isinstance(spider, Tieba3Spider):
                # 处理其中的titie poster
                # '点0\xa0回2\xa0请填密码asd\xa011:05' --> '点0 回2 请填密码asd 11:05'
                item['poster'] = item['poster'].replace(u'\xa0', ' ')
                item['poster'] = re.search(r"回\d+\s(.*?)\s", item['poster']).group(1)
                # '19.\xa0这张图的正确解读是什么' --> '19. 这张图的正确解读是什么'
                item['title'] = item['title'].replace(u'\xa0', ' ')
                item['title'] = re.search(r'\d+\.\s(.*)$', item['title']).group(1)

            return item  # 这里就算不写return，数据照样还会传给下一个pipeline


class MongoPipeline:
    """保存数据到mongo数据库"""

    def process_item(self, item, spider):
        # 这里有的item竟然会变成None，不知为何❌❌
        if item is None:
            return

        if item['poster'] and item['title']:
            # 存入数据库
            self.collection.insert_one(dict(item))  # 插入前将item转成dict
            print(item)
            print()

        return item

    def open_spider(self, spider):  # 爬虫启动时会调用该函数
        # 实例化mongo客户端
        client = MongoClient(host=spider.settings.get("MONGO_HOST"),
                             port=spider.settings.get("MONGO_PORT"))
        # 获取collection
        self.collection = client[spider.settings.get("MONGO_DB")][spider.settings.get("MONGO_COLLECTION")]
