import scrapy
from book.items import BookItem
from copy import deepcopy


# 由于scrapy是异步的，对于需要使用meta传递的item，最好每次都是用deepcopy，防止出错✅

class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['http://suning.com/']

    def parse(self, response):  # 处理起始页，从起始页中提取大分类、小分类、以及小分类对应的url
        # 分组
        div_list = response.xpath()
        # 获取大分类
        for div in div_list:
            main_cate = div.xpath()
            # 分组
            li_list = div.xpath()
            # 获取小分类
            for li in li_list:
                item = BookItem()
                item["sub_cate"] = li.xpath()
                item["sub_cate_url"] = li.xpath()
                item["main_cate"] = main_cate
                # 将大分类，小分类，和小分类的url传给别的解析函数
                if item["sub_cate_url"]:
                    yield scrapy.Request(
                        item["sub_cate_url"],
                        callback=self.parse_list,
                        meta=dict(item=deepcopy(item))  # ✅
                    )

    def parse_list(self, response):  # 处理小分类的列表页
        # 从上一个解析函数中取数据
        item = response.meta["item"]
        # 分组
        div_list = response.xpath()
        # 获取每个图书的标题、作者、出版社、简介、和详情页的url
        for div in div_list:
            item["title"] = div.xpath()
            item["author"] = div.xpath()
            item["publisher"] = div.xpath()
            item["abstract"] = div.xpath()
            item["detail_url"] = div.xpath()
            yield scrapy.Request(
                item["detail_url"],
                callback=self.parse_detail,
                meta=dict(item=deepcopy(item))  # 这里也要deepcopy ✅
            )
        # 获取下一个列表页的url
        next_url = response.xpath()
        if next_url:
            # 下一个列表页也需要原始的item信息
            yield scrapy.Request(
                next_url,
                callback=self.parse_list,
                meta=dict(item=deepcopy(item))  # 这里也要deepcopy ✅
            )

    def parse_detail(self, response):  # 从详情页提取数据
        item = response.meta["item"]
        # 提取价格
        item["price"] = response.xpath()
        yield item  # 将最终的数据传给pipeline
