# scrapy版本的贴吧爬虫
import scrapy


class Tieba2Spider(scrapy.Spider):
    name = 'tieba2'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/']

    def parse(self, response):
        pass
