# 手动构造表单数据
import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        # 提取表单数据
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        login = "820710063@qq.com"
        password = "liulei666666@yeah.net"
        trusted_device = response.xpath("//input[@name='trusted_device']/@value").extract_first()
        webauthn_support = response.xpath("//input[@name='webauthn-support']/@value").extract_first()
        webauthn_iuvpaa_support = response.xpath("//input[@name='webauthn-iuvpaa-support']/@value").extract_first()
        return_to = response.xpath("//input[@name='return_to']/@value").extract_first()
        allow_signup = response.xpath("//input[@name='allow_signup']/@value").extract_first()
        client_id = response.xpath("//input[@name='client_id']/@value").extract_first()
        integration = response.xpath("//input[@name='integration']/@value").extract_first()
        required_field_key = re.search(r'name="(required_field_.*?)"', response.text).group(1)
        required_field_value = response.xpath("//input[contains(@name, 'required_field')]/@value").extract_first()
        timestamp = response.xpath("//input[@name='timestamp']/@value").extract_first()
        timestamp_secret = response.xpath("//input[@name='timestamp_secret']/@value").extract_first()

        # 构造表单数据
        form_data = dict(commit=commit, authenticity_token=authenticity_token, login=login,
                         password=password, trusted_device=trusted_device, return_to=return_to,
                         allow_signup=allow_signup, client_id=client_id, integration=integration,
                         timestamp=timestamp, timestamp_secret=timestamp_secret)
        form_data["webauthn-support"] = webauthn_support
        form_data["webauthn-iuvpaa-support"] = webauthn_iuvpaa_support
        form_data[required_field_key] = required_field_value

        # 构造form表单数据时，如果有些键的值为空，必须改成空字符串，不能用None，否则会报错。
        # TypeError: to_bytes must receive a str or bytes object, got NoneType
        for key in form_data:
            if form_data[key] is None:
                form_data[key] = ""

        print(form_data)

        # 发送post请求
        return scrapy.FormRequest(url="https://github.com/session", formdata=form_data, callback=self.after_login)

    def after_login(self, response):
        # 查看登录后的url，登录后被跳转到github.com
        print(response.url, "*" * 100, response.status)
        #  <200 https://github.com/>

        # print(response.headers)
        print(re.findall(r"kenzzuli", response.text))
        # ['kenzzuli', ... , 'kenzzuli', 'kenzzuli']
        yield scrapy.Request(url="https://github.com/dashboard/top_repositories?location=center",
                             callback=self.check_dashboard)

    def check_dashboard(self, response):
        # print(response.url, "*" * 100, response.status)
        print(response.xpath("//li[@class='public source ']//a/@href").extract())
        # ['/kenzzuli/hm_15', '/kenzzuli/chat_service', '/kenzzuli/seq2seq_demo', '/kenzzuli/train_bert_model_from_scratch']
