import scrapy


class HrSpider(scrapy.Spider):
    # 实际爬的是百度关于python的搜索结果，因为腾讯招聘网址对应的响应和elments中的内容不一样。
    name = 'hr'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=python']

    def parse(self, response):
        div_list = response.xpath("//div[@id='content_left']/div")
        for div in div_list:
            item = dict()
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

    def parse1(self, response):
        pass
