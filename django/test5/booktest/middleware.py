from django.http import HttpResponse


class BlockedIPsMiddleware:
    """中间件类"""
    # ip地址黑名单
    EXCLUDE_IPS = ["202.121.96.187"]

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """中间件函数，视图函数调用之前会调用此函数"""
        if request.META['REMOTE_ADDR'] in self.EXCLUDE_IPS:
            return HttpResponse("<h1>Forbidden</h1>")


class TestMiddleware:
    """测试中间件类"""

    def __init__(self):
        """服务器重启之后，接收第一个请求时调用"""
        print("---init---")

    def process_request(self, request):
        """产生request对象之后, url匹配之前调用"""
        print("---process_request---")
        # return HttpResponse('process_request')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """url匹配之后，调用view函数之前被调用"""
        print("---process_view---")
        return HttpResponse('process_view')

    def process_response(self, request, response):
        """view函数调用之后，response返回给浏览器之前被调用"""
        print("---process_response---")
        return response


class ExceptionTest1Middleware:
    def process_exception(self, request, exception):
        """视图函数发生异常时调用"""
        print("---process_exception1")
        print(exception)


class ExceptionTest2Middleware:
    def process_exception(self, request, exception):
        """视图函数发生异常时调用"""
        print("---process_exception2")
