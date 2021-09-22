# 银保监会行政处罚
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class PunishmentSpider(CrawlSpider):
    name = 'punishment'
    allowed_domains = ['cbirc.gov.cn']
    start_urls = [
        'http://www.cbirc.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=4113&itemUrl=ItemListRightList.html&itemName=%E9%93%B6%E4%BF%9D%E7%9B%91%E4%BC%9A%E6%9C%BA%E5%85%B3&itemsubPId=931&itemsubPName=%E8%A1%8C%E6%94%BF%E5%A4%84%E7%BD%9A']

    # 定义提取url地址规则
    rules = (
        # LinkExtractor: 连接提取器用于提取url
        # callback:提取url地址的响应会交给callback对应的解析函数来提取，可以不写
        # follow:提取url地址的响应是否会再次经过rules来提取url，可以不写，默认为false

        # 这里提取详情页的url，并将url对应的响应交给callback函数处理
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item'),
        # 这里提取下一个列表页的url，并将url对应的响应（即第二页的列表页）继续交给rules来提取url，达到了翻页的效果
        Rule(LinkExtractor(allow=r'Items/'), follow=True),
    )

    # parse函数有特殊功能，这里不能重写parse函数。
    def parse_item(self, response):  # 这里从详情页的响应中提取数据
        item = {}

        item["title"] = re.findall("", response.body.decode())[0]
        item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        item['name'] = response.xpath('//div[@id="name"]').get()
        item['description'] = response.xpath('//div[@id="description"]').get()
        url = response.xpath()
    #     # 如果这里提取的数据仍然不完整，可以接着yield
    #     yield scrapy.Request(
    #         url,
    #         callback=self.parse_detail,
    #         meta=dict(item=item)
    #     )
    #
    # def parse_detail(self, response):  # 接着上面的解析函数，继续提取数据
    #     item = response.meta["item"]
    #     item["price"] = response.xpath()
    #     yield item
