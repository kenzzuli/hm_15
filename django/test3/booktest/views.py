from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from datetime import datetime, timedelta


# request就是HttpRequest类型的对象
# 包含浏览器请求的信息
# Create your views here.
def index(request):
    """首页"""
    # num = "a" + 1
    print(request.method)  # GET
    print(request.path)  # /index
    return render(request, 'booktest/index.html')


def show_arg(request, arg):
    """显示参数"""
    return HttpResponse(arg)


def login(request):
    """登录页面"""
    # 判断用户是否已经登录
    islogin = request.session.get('islogin', False)
    if islogin:
        # 用户已经登录，跳转到首页
        return redirect('/index')
    else:
        # 记住用户名
        # 获取cookie中的username，如果不存在，则为""
        username = request.COOKIES.get('username', "")
        return render(request, 'booktest/login.html', context=dict(username=username))


def login_check(request):
    """登录校验"""
    # request.POST保存的是post提交的参数
    # request.GET保存的是get提交的参数
    # 1.获取提交的用户名和密码
    # print(type(request.POST))
    # <class 'django.http.request.QueryDict'>
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 获取是否记住用户名，如果勾选，结果为on，如果不勾选结果为None
    remember = request.POST.get('remember')
    print(remember)  # on
    print(username, password)  # admin liulei123
    print(request.method)  # POST
    print(request.encoding)  # None
    print(request.COOKIES)
    # {'csrftoken': 'CmQ1JE1LyivzHQzUPGRfncBxz94ns9bf', 'sessionid': 'r23bsdjbjl1frslf5wpatgzachfr2fm5'}
    print(request.session)  # <django.contrib.sessions.backends.db.SessionStore object at 0x7fec3a080f28>
    # 2.登录校验
    # 实际开发中，根据用户名和密码查找数据库
    # 模拟，用户名为admin，密码为liulei123
    if username == 'admin' and password == 'liulei123':
        # 用户名密码正确，则跳转到首页
        response = redirect('/index')
        # 如果设置了记住用户名
        if remember == 'on':
            # 设置cookie username， 过期时间为一周
            response.set_cookie('username', username, max_age=7 * 24 * 3600)
        # 记住用户登录状态
        # 只要session中有islogin，就认为用户已经登录
        request.session['islogin'] = True
        # 返回响应
        return response
    else:
        # 用户名密码或错误，跳转到登录页
        return redirect('/login')


def test_ajax(request):
    """显示ajax页面"""
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(request):
    """ajax请求处理"""
    # num = 'a' + 1
    # 返回的json数据 {'res':1}
    return JsonResponse({'res': 1})


def login_ajax(request):
    """ajax登录"""
    return render(request, 'booktest/login_ajax.html')


def login_check_ajax(request):
    """ajax登录校验"""
    # 1.获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 2.进行校验，返回数据
    if username == 'admin' and password == 'liulei123':
        return JsonResponse({'res': 1})
        # return redirect('/index') # ajax请求在后台，不要返回页面或重定向
    else:
        return JsonResponse({'res': 0})


def set_cookies(request):
    """设置cookie信息"""
    response = HttpResponse("设置cookie")
    # 设置一个cookie，key为name， value为liulei
    # 过期时间，多少秒后过期
    response.set_cookie('name', 'liulei', max_age=14 * 24 * 3600)
    # 过期时间，指定过期时间  datetime.datetime(2021, 10, 4, 10, 47, 25, 832120)
    response.set_cookie('gender', 'male', expires=datetime.now() + timedelta(days=14))
    return response


def get_cookies(request):
    """读取cookies信息"""
    name = request.COOKIES['name']
    gender = request.COOKIES['gender']
    # 取出cookie
    return HttpResponse(name + " " + gender)


def set_session(request):
    """设置session"""
    request.session['username'] = "admin"
    request.session['age'] = 18
    request.session.set_expiry(5)
    return HttpResponse("设置session")


def get_session(request):
    """获取session"""
    username = request.session.get('username', "")
    age = request.session.get('age', "")
    return HttpResponse(str(username) + " " + str(age))


def clear_session(request):
    """清除session"""
    request.session.clear()
    return HttpResponse("清除session")


def flush_session(request):
    """清空session"""
    request.session.flush()
    return HttpResponse("清空session")
