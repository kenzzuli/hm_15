# scrapy版本的贴吧爬虫
# 从列表页提取发帖人，标题
import scrapy
from tieba.items import TiebaItem


class Tieba3Spider(scrapy.Spider):
    name = 'tieba3'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=%E6%9D%8E%E6%AF%85&pn=0']

    def parse(self, response):
        # 根据帖子进行分组
        div_list = response.xpath("//div[contains(@class,'i')]")
        for div in div_list:
            item = TiebaItem()
            # 获取每个帖子的url
            item['url'] = div.xpath("./a/@href").extract_first()
            # 获取标题
            item['title'] = div.xpath("./a/text()").extract_first()
            # 获取发帖人
            item['poster'] = div.xpath("./p/text()").extract_first()
            # 构造img字段 ✅
            item['img_url_list'] = list()
            # 判断帖子的url是否为空
            if item['url']:
                item['url'] = response.urljoin(item['url'])
                yield scrapy.Request(url=item['url'], callback=self.parse_post, meta=dict(item=item))  # url不完整，需补全

            # 获取列表页下一页的地址
            next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
            if next_url:
                yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse)

    def parse_post(self, response):
        # 这里的item要么是从上一个parse_post函数传来，要么从parse函数传来，都携带有item
        item = response.meta['item']

        # 将帖子当前页中的图片url追加到列表中 ✅
        item['img_url_list'] += response.xpath("//img[@class='BDE_Image']/@src").extract()

        # 获取帖子下一页的url
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        # 判断帖子是否还有下一页
        if next_url:  # 如果有 继续发送请求，提取数据
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_post, meta=dict(item=item))
        else:  # 如果没有，将item传到pipeline
            yield item
