import scrapy
from tencent.items import TencentItem  # 导入items中自定义的item类


class HrSpider(scrapy.Spider):
    # 实际爬的是百度关于python的搜索结果，因为腾讯招聘网址对应的响应和elments中的内容不一样。
    name = 'hr'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=python']

    def parse(self, response):
        print(response)
        div_list = response.xpath("//div[@id='content_left']/div")
        print(div_list)
        for div in div_list:
            item = TencentItem()
            # 这里的字段必须是TencentItem中定义好的字段
            item["title"] = "".join(div.xpath(".//a//text()").extract())
            item["url"] = div.xpath(".//a/@href").extract_first()
            print(item)
            print("*" * 50)
            yield item
        # 找到next_url
        next_url = response.xpath("//a[contains(text(),'下一页')]/@href").extract_first()
        print("-" * 50)
        if next_url:
            next_url = "https://www.baidu.com" + next_url
            yield scrapy.Request(next_url, callback=self.parse)
            # callback指明下一页url的响应由哪个函数处理
            # 如果下一页的响应和起始页的响应相同，则还由当前函数处理
            # 如果下一页的响应和起始页的响应不同，则自定义一个函数，并将该函数传给callback
            # yield scrapy.Request(next_url, callback=self.parse1)

            # 如果一个parse函数得到的数据不完整，需要将数据在不同的解析函数中传递，可以使用meta参数，meta接收一个字典
            # 假如这个函数仅提取了列表页的信息，但还有部分信息在详情页，二者结合才能组成一个完整的字典
            # 通过meta参数将列表页的信息传给下一个解析函数
            # yield scrapy.Request(next_url, callback=self.parse1, meta={"item": item})

    def parse1(self, response):
        # 接收列表页的信息，在这个解析函数中提取详情页信息，然后组装成完成的item
        item = response.meta["item"]
        pass
