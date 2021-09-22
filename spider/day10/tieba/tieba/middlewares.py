# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random


class RandomUserAgentMiddleware:
    """添加随机用户代理"""

    def process_request(self, request, spider):
        user_agent = random.choice(spider.settings.get("USER_AGENTS_LIST"))
        request.headers["User-Agent"] = user_agent


class CheckUserAgent:
    """检查是否使用了随机用户代理"""

    def process_response(self, request, response, spider):
        # 查看response.request中的方法和属性，发现并没有headers属性
        # print(dir(response.request))

        # 只有request中有headers属性
        # print(request.headers["User-Agent"])

        # 最后必须return response或request ✅
        return response
