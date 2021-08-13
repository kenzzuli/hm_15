# 百度贴吧crawl spider版本
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tieba.items import TiebaItem


class TbSpider(CrawlSpider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=%E6%9D%8E%E6%AF%85&pn=0']
    rules = (
        # 翻页
        Rule(LinkExtractor(allow=r'm?kw=%E6%9D%8E%E6%AF%85&lp=\d+&lm=&pn=\d+'), follow=True),
        # 获取每个帖子的链接
        Rule(LinkExtractor(allow=r'm?kz=\d+&is_bakan=\d+&lp=\d+&pinf=\d+_\d+_\d+'), callback='parse_item'),
    )

    def parse_item(self, response):
        # 通过meta中是否有item来判断是否是首次调用
        item = response.meta.get('item', None)
        # 如果是首次调用
        if not item:
            item = TiebaItem()
            item['img_url_list'] = list()  # 帖子中所有图片的url
            item['url'] = response.url  # 当前帖子的url
            item['title'] = response.xpath("//div[@class='bc p']/strong/text()").extract_first()  # 帖子标题
            item['poster'] = response.xpath(
                "//div[@class='d']/div[1]//span[@class='g']//a/text()").extract_first()  # 发帖人

        # 将帖子当前页中的图片url加入列表中
        item['img_url_list'] += response.xpath("//img[@class='BDE_Image']/@src").extract()
        # 获取帖子下一页的url
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()

        # 判断帖子是否还有下一页
        if next_url:  # 如果有 继续发送请求，提取数据
            next_url = response.urljoin(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse_item, meta=dict(item=item))
        else:  # 如果没有，将item传到pipeline
            yield item
