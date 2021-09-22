# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AozoraScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    file_urls = scrapy.Field()  # 这两个字段是FilesPipeline要求的
    files = scrapy.Field()
    pass
