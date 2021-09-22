import scrapy
from yangguang.items import YangguangItem


class PoliticsSpider(scrapy.Spider):
    name = 'politics'
    allowed_domains = ['sun0769.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest']  # start_urls可以不满足allowed_domain
    base_url = "https://wz.sun0769.com"

    def parse(self, response):
        # spider自身有settings属性
        # 在pipeline中的open_spider中给爬虫设置属性hello，在爬虫中可以使用该属性
        print(self.hello)
        print(self.settings["MONGO_HOST"])
        print(self.settings.get("MONGO_HOST", None))
        print("-" * 50)
        # 分组
        li_list = response.xpath("//ul[@class='title-state-ul']/li")
        for li in li_list:
            item = YangguangItem()
            item["num"] = li.xpath("./span[@class='state1']/text()").extract_first()
            item["status"] = li.xpath("./span[@class='state2']/text()").extract_first()
            item["title"] = li.xpath("./span[@class='state3']/a/text()").extract_first()
            item["detail_url"] = self.base_url + li.xpath("./span[@class='state3']/a/@href").extract_first()
            item["response_time"] = li.xpath("./span[@class='state4']/text()").extract_first()
            item["post_time"] = li.xpath("./span[@class='state5 ']/text()").extract_first()
            # 将列表页的数据传给详情页的解析函数
            yield scrapy.Request(item["detail_url"], callback=self.parse_detail, meta=dict(item=item))

        # 翻页
        next_url = response.xpath("//a[@class='arrow-page prov_rota']/@href").extract_first()
        if next_url:
            yield scrapy.Request(self.base_url + next_url, callback=self.parse)

    def parse_detail(self, response):
        # 提取详情页的信息
        item = response.meta["item"]
        item["detail"] = response.xpath("//div[@class='details-box']/pre/text()").extract_first()
        item["img_url"] = response.xpath("//div[@class='clear details-img-list Picture-img']/img/@src").extract()
        yield item
