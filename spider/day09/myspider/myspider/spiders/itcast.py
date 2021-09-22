import scrapy
import logging

logger = logging.getLogger(__name__)


# 一个项目里可以有多个爬虫
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/']

    def parse(self, response):
        for i in range(10):
            item = dict()
            item["come_from"] = self.name

            # 通过日志将item输出
            # logging.warning(item)
            # 显示的root表示根目录，但我们不知道日志来自哪个py文件
            # 2021-07-17 22:57:53 [root] WARNING: {'come_from': 'itcast'}

            # 使用logger
            logger.warning(item)
            # 2021-07-17 23:03:16 [myspider.spiders.itcast] WARNING: {'come_from': 'itcast'}
            # 显示出该条日志来自哪个py文件

            yield item
