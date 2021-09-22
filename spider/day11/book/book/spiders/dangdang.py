import scrapy
from scrapy_redis.spiders import RedisSpider
from copy import deepcopy


class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # 程序会从redis_key对应的值中读取start_url
    # 在redis客户端输入 lpush dangdang http://book.dangdang.com/
    redis_key = "dangdang"

    def parse(self, response):
        # 大分类分组
        div_list = response.xpath("//div[@class='con flq_body']/div")
        for div in div_list:
            cate_b = div.xpath("./dl/dt//text()").extract()
            # cate_b = [i.strip() for i in cate_b if i.strip()]
            cate_b = "".join([i.strip() for i in cate_b if i.strip()]).replace('\xa0', "")
            # 中分类分组
            dl_list = div.xpath(".//div[contains(@class, 'submenu')]//dl")
            for dl in dl_list:
                cate_m = dl.xpath("./dt//text()").extract()
                cate_m = "".join([i.strip() for i in cate_m if i.strip()]).replace("\xa0", "")
                # 小分类分组
                a_list = dl.xpath("./dd/a")
                for a in a_list:
                    cate_s = a.xpath("./@title").extract_first()
                    cate_s_url = a.xpath("./@href").extract_first()
                    item = dict(cate_b=cate_b, cate_m=cate_m, cate_s=cate_s, cate_s_url=cate_s_url)
                    if cate_s_url:
                        yield scrapy.Request(cate_s_url, meta=dict(item=item), callback=self.parse_booklist)

    def parse_booklist(self, response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='con shoplist']//ul/li")
        for li in li_list:
            # 这里即使还用item，不使用item_new也没问题，因为三个分类信息不变，而书籍信息每次循环都会更新
            item_new = deepcopy(item)
            item_new["book_img"] = response.urljoin(li.xpath("./a[@class='pic']/img/@data-original").extract_first())
            item_new["book_name"] = li.xpath("./p[@class='name']/a/@title").extract_first()
            item_new["book_detail"] = li.xpath("./p[@class='detail']/text()").extract_first()
            item_new["book_price"] = li.xpath("./p[@class='price']/span/text()").extract_first()
            item_new["book_seller"] = li.xpath("./p[@class='search_shangjia']/a/text()").extract_first()
            item_new["book_author"] = li.xpath("./p[@class='search_book_author']/span[1]/a/text()").extract()
            item_new["book_pub_date"] = \
                li.xpath("./p[@class='search_book_author']/span[2]/text()").extract_first()
            if item_new["book_pub_date"]:
                item_new["book_pub_date"] = item_new["book_pub_date"].split("/")[-1]
            item_new["book_press"] = li.xpath("./p[@class='search_book_author']/span[3]/a/text()").extract_first()

            print(item_new)
            print("-" * 50)
            yield item_new
        # 翻页
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_url:
            yield scrapy.Request(response.urljoin(next_url), meta=dict(item=item), callback=self.parse_booklist)
