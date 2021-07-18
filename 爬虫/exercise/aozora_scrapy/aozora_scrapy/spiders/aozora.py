import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os
from aozora_scrapy.items import AozoraScrapyItem


class AozoraSpider(CrawlSpider):
    name = 'aozora'
    allowed_domains = ['aozora.gr.jp']
    start_urls = ['https://www.aozora.gr.jp/']

    rules = (
        # 规则的顺序不能反过来，不然就一直爬，提取不到详情页了
        Rule(LinkExtractor(allow=r'cards/\d+/.*?\.html'), callback='parse_item'),  # 先提取详情页
        Rule(LinkExtractor(), follow=True),  # 再不停爬
    )

    def parse_item(self, response):
        file_url = response.xpath("//a[contains(@href, '.zip')]/@href").extract_first()
        if file_url:
            file_url = response.urljoin(file_url)
            item = AozoraScrapyItem()
            item["file_urls"] = [file_url]
            yield item
