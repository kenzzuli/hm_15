import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/327550029/profile']

    def start_requests(self):
        """重写start_request，该方法用于为start_urls发送请求"""

        cookies = "BIDUPSID=A9ED107CDA04315473528F700F5BB884; PSTM=1602854207; BAIDUID=A9ED107CDA04315459EF911AEED8EAB0:FG=1"
        # 将字符串转成字典
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        # 在发送请求时，加上cookies参数
        yield scrapy.Request(self.start_urls[0], callback=self.parse, cookies=cookies)

    def parse(self, response):
        print(re.findall("毛兆军", response.body.decode()))

        # 如果再次请求新的页面，查看是否携带了cookie
        yield scrapy.Request(
            "http://www.renren.com/327550029/profile?v=info+timeline",
            callback=self.parse_detail
        )

    def parse_detail(self, response):
        print(re.findall("毛兆军", response.body.decode()))
