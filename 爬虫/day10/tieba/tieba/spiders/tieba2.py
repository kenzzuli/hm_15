# scrapy版本的贴吧爬虫
import scrapy
from tieba.items import TiebaItem


class Tieba2Spider(scrapy.Spider):
    name = 'tieba2'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=%E6%9D%8E%E6%AF%85&pn=0']

    def parse(self, response):
        # 根据帖子进行分组
        div_list = response.xpath("//div[contains(@class,'i')]")
        for div in div_list:
            item = TiebaItem()
            # 获取每个帖子的url
            post_url = div.xpath("./a/@href").extract_first()
            if post_url:
                item['url'] = response.urljoin(post_url)
                yield scrapy.Request(url=item['url'], callback=self.parse_post, meta=dict(item=item))  # url不完整，需补全

            # 获取列表页下一页的地址
            next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
            if next_url:
                yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse)

    def parse_post(self, response):
        item = response.meta['item']
        # 通过是否存在title字段来判断是否是帖子的第一页
        if not item.get('title', None):
            item['img_url_list'] = list()
            item['title'] = response.xpath("//div[@class='bc p']/strong/text()").extract_first()
            item['poster'] = response.xpath(
                "//div[@class='d']/div[1]//span[@class='g']//a/text()").extract_first()

        # 将帖子当前页中的图片url加入列表中
        item['img_url_list'] += response.xpath("//img[@class='BDE_Image']/@src").extract()

        # 获取帖子下一页的url
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        # 判断帖子是否还有下一页
        if next_url:  # 如果有 继续发送请求，提取数据
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_post, meta=dict(item=item))
        else:  # 如果没有，将item传到pipeline
            yield item
