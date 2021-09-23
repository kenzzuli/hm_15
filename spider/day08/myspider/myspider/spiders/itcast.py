import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名
    allowed_domains = ['itcast.cn']  # 允许爬取的范围
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml']  # 最开始请求的url地址

    def parse(self, response):  # 函数名必须是parse，否则NotImplementedError: ItcastSpider.parse callback is not defined
        # 处理start_url对应的响应
        ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # 就算xpath写错，没有数据，使用extract方法也不会报错，得到的结果是一个空列表
        # print(ret1)

        # 分组
        li_list = response.xpath("//div[@class='tea_con']//li")  # xpath之后的结果是一个列表
        # content_list = list()
        for li in li_list:
            item = {}
            # 这种列表有extract方法，得到的结果还是一个列表，然后取第0个元素
            # item["name"] = li.xpath(".//h3/text()").extract()[0]
            # item["title"] = li.xpath(".//h4/text()").extract()[0]
            # extract_first方法，从列表中提取第0个元素
            # 就算xpath写错，没有结果，使用extract_first方法也不会报错，结果为None
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            # print(item)
            # content_list.append(item)

            # 将spider的结果传给pipeline
            yield item

        # 不能返回列表
        # yield content_list
        # ERROR: Spider must return request, item, or None, got 'list'