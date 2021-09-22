# 自动寻找表单
import scrapy
import re


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        # 自动从response中寻找表单
        yield scrapy.FormRequest.from_response(
            response,
            formdata={"login": "820710063@qq.com",
                      "password": "liulei666666@yeah.net"},
            callback=self.after_login
        )

    def after_login(self, response):
        # 查看登录后的url，登录后被跳转到github.com
        # print(response.url, "*" * 100, response.status)
        #  <200 https://github.com/>

        print(re.findall(r"kenzzuli", response.text))
        # ['kenzzuli', ... , 'kenzzuli', 'kenzzuli']
        yield scrapy.Request(url="https://github.com/dashboard/top_repositories?location=center",
                             callback=self.check_dashboard)

    def check_dashboard(self, response):
        print(response.xpath("//li[@class='public source ']//a/@href").extract())
        # ['/kenzzuli/hm_15', '/kenzzuli/chat_service', '/kenzzuli/seq2seq_demo', '/kenzzuli/train_bert_model_from_scratch']
