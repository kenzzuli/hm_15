import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
import re


# todo 其实可以在图书详情页提取全部信息，而不必在列表页提取任何信息

class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    redis_key = 'amazon'
    # start_urls = ["https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=sd_allcat_books_l1?ie=UTF8&node=658390051"]
    # 在redis客户端输入 lpush amazon https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=sd_allcat_books_l1?ie=UTF8&node=658390051

    rules = (
        # 使用xpath写规则
        # 同时匹配大分类、小分类
        Rule(LinkExtractor(restrict_xpaths=("//li[@class='a-spacing-micro apb-browse-refinements-indent-2']",)),
             follow=True),
        # 进入列表页
        Rule(LinkExtractor(restrict_xpaths=("//span[@class='a-size-medium a-color-link a-text-bold']/..",)),
             callback='parse_item', follow=True),
        # 列表页翻页
        Rule(LinkExtractor(restrict_xpaths=("//div[@role='navigation']",), ), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # cate_info = response.xpath("//ul[@aria-labelledby='n-title']/li//text()").extract()[1:]
        # cate_info = [i.strip().replace('\xa0', '') for i in cate_info if i.strip().replace('\xa0', '')]
        cate_url = response.url
        # 分组
        div_list = response.xpath("//div[@data-component-type='s-search-result']")
        for div in div_list:
            book_img = div.xpath(".//img[@class='s-image']/@src").extract_first()
            book_title = div.xpath(".//h2/a/span/text()").extract_first()
            book_url = response.urljoin(div.xpath(".//h2/a/@href").extract_first())
            book_author = div.xpath(".//div[@class='a-row']/span[@class='a-size-base']/text()").extract()
            book_author = [i.strip() for i in book_author if i != '、 ' and i.strip()]
            book_pub_date = div.xpath(".//div[@class='a-row']/span[last()]/text()").extract_first()
            book_rate = div.xpath(".//div[@class='a-row a-size-small']/span[1]/@aria-label").extract_first()
            if book_rate:
                book_rate = re.search(r'^(.*?)\s颗星', book_rate).group(1)
            book_comment_num = div.xpath(".//div[@class='a-row a-size-small']/span[2]/@aria-label").extract_first()
            book_price = div.xpath(".//span[@class='a-price']/span[1]/text()").extract_first()
            book_seller = div.xpath(
                ".//span[@class='s-self-operated aok-align-bottom aok-inline-block a-text-normal']/text()").extract_first()
            item = dict(
                # cate_info=cate_info,
                cate_url=cate_url, book_img=book_img, book_title=book_title,
                book_url=book_url, book_author=book_author, book_pub_date=book_pub_date,
                book_rate=book_rate, book_comment_num=book_comment_num, book_price=book_price,
                book_seller=book_seller
            )
            yield scrapy.Request(book_url, callback=self.parse_book_detail, meta=dict(item=item))

    def parse_book_detail(self, response):
        file_name = response.url.replace("/", "") + ".html"
        with open(file_name, mode='w', encoding='utf8') as f:
            f.write(response.text)
        item = response.meta['item']
        book_publisher = response.xpath(
            "//div[@id='detailBullets_feature_div']/ul/li[2]/span/span[2]/text()").extract_first()
        book_publisher = book_publisher.split(";")[0] if book_publisher else None
        item['book_publisher'] = book_publisher
        cate_info = response.xpath("//ul[@class='a-unordered-list a-horizontal a-size-small']//a/text()").extract()
        cate_info = [i.strip() for i in cate_info if i.strip()]
        item['cate_info'] = cate_info
        print(item)
        print("-" * 50)
        yield item
