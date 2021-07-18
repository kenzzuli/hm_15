# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num = scrapy.Field()
    status = scrapy.Field()
    title = scrapy.Field()
    detail_url = scrapy.Field()
    response_time = scrapy.Field()
    post_time = scrapy.Field()
    detail = scrapy.Field()
    img_url = scrapy.Field()
