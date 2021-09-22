# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    main_cate = scrapy.Field()  # 图书的大分类名
    sub_cate = scrapy.Field()  # 图书的小分类名
    sub_cate_url = scrapy.Field()  # 图书的小分类对应的url
    title = scrapy.Field()  # 图书的标题
    author = scrapy.Field()  # 图书的作者
    publisher = scrapy.Field()  # 出版社
    abstract = scrapy.Field()  # 简要介绍
    detail_url = scrapy.Field()  # 详情页url
    price = scrapy.Field()  # 图书价格

    pass
