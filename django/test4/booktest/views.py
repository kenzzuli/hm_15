from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse
from booktest.models import BookInfo
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
from string import ascii_letters, digits
from django.core.urlresolvers import reverse


# Create your views here.
# /verify_code
def verify_code(request):
    """生成验证码"""
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = ascii_letters + digits
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，mac中查看字体列表 fc-list
    font = ImageFont.truetype('Times New Roman.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


# /verify_show
def verify_show(request):
    """验证页面"""
    return render(request, 'booktest/verify_show.html')


# /verify_yz
def verify_yz(request):
    """处理用户提交的验证码"""
    if request.session.get('verifycode').lower() == request.POST.get('yzm').lower():
        return HttpResponse("验证通过")
    else:
        return redirect("/verify_show")


def login_required(view_func):
    """登录判断装饰器"""

    def wrapper(request, *args, **kwargs):
        # 如果已登录，则调用相应的视图
        if 'islogin' in request.session:
            return view_func(request, *args, **kwargs)
        # 如果未登录，则跳转到登录页
        else:
            return redirect('/login')

    return wrapper


def my_render(request, template_path, context={}):
    # 1.加载模板文件，获取一个模板对象
    template = loader.get_template(template_path)
    # 2.定义模板上下文，给模板文件传数据
    context = RequestContext(request, context)
    # 3.模板渲染，产生一个替换后的html内容
    res_html = template.render(context)
    # 4.返回应答
    return HttpResponse(res_html)


# /index
def index(request):
    # return my_render(request, 'booktest/index.html')
    return render(request, 'booktest/index.html')


# /index2
def index2(request):
    """查看模板文件的加载顺序"""
    return render(request, 'booktest/index2.html')


# /tem_var
def tem_var(request):
    """模板变量"""
    my_dict = {'title': '字典键值'}  # 字典
    my_list = [1, 2, 3]  # 列表
    book = BookInfo.objects.get(id=1)  # 对象
    return render(request, 'booktest/tem_var.html',
                  dict(my_dict=my_dict, my_list=my_list, book=book))


# /tem_tag
def tem_tag(request):
    """模板标签"""
    # 查找所有图书的信息
    books = BookInfo.objects.all()
    return render(request, 'booktest/tem_tag.html',
                  dict(books=books))


# /tem_filter
def tem_filter(request):
    """模板过滤器"""
    # 查找所有图书的信息
    books = BookInfo.objects.all()
    return render(request, 'booktest/tem_filter.html',
                  dict(books=books))


# /tem_inherit
def tem_inherit(request):
    """模板继承"""
    return render(request, 'booktest/child.html')


# /html_escape
def html_escape(request):
    """html转义"""
    return render(request, 'booktest/html_escape.html',
                  {'content': '<h1>hello</h1>'})


# /login
def login(request):
    """登录页面"""
    # 判断用户是否已经登录
    islogin = request.session.get('islogin', False)
    if islogin:
        # 用户已经登录，跳转到修改密码页面
        return redirect('/change_pwd')
    else:
        # 记住用户名
        # 获取cookie中的username，如果不存在，则为""
        username = request.COOKIES.get('username', "")
        return render(request, 'booktest/login.html', dict(username=username))


# /login_check
def login_check(request):
    """登录校验"""
    # 1.获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 获取是否记住用户名，如果勾选，结果为on，如果不勾选结果为None
    remember = request.POST.get('remember')

    # 获取验证码
    # session中保存的验证码
    code_generated = request.session.get('verifycode')
    # 用户输入的验证码
    code_input = request.POST.get('yzm')

    # 验证码校验
    if code_input.lower() != code_generated.lower():
        # 验证码错误，跳转到登录页面
        return redirect('/login')

    # 2.登录校验
    # 实际开发中，根据用户名和密码查找数据库
    # 模拟，用户名为admin，密码为liulei123
    if username == 'admin' and password == 'liulei123':
        # 用户名密码正确，则跳转到修改密码页面
        response = redirect('/change_pwd')
        # 如果设置了记住用户名
        if remember == 'on':
            # 设置cookie username， 过期时间为一周
            response.set_cookie('username', username, max_age=7 * 24 * 3600)
        # 记住用户登录状态
        # 只要session中有islogin，就认为用户已经登录
        request.session['islogin'] = True
        # 此外，在session中记录用户名
        request.session['username'] = username
        # 返回响应
        return response
    else:
        # 用户名密码或错误，跳转到登录页
        return redirect('/login')


# /change_pwd
@login_required
def change_pwd(request):
    """显示修改密码页面"""

    # # 进行用户登录的判断，只有登录用户，才可以访问修改密码页面
    # if 'islogin' not in request.session:
    #     return redirect('/login')

    return render(request, "booktest/change_pwd.html")


# /change_pwd_action
@login_required
def change_pwd_action(request):
    """处理修改密码"""

    # # 进行用户登录的判断，只有登录用户，才可以访问此页面
    # if 'islogin' not in request.session:
    #     return redirect('/login')

    # 1.获取新密码
    new_pass = request.POST.get('pwd')
    # 2.实际开发时，修改对应数据库中的内容
    # 3.返回一个应答
    username = request.session.get('username')
    return HttpResponse("%s 修改密码为 %s" % (username, new_pass))


# /url_reverse
def url_reverse(request):
    """url反向解析"""
    return render(request, 'booktest/url_reverse.html')


# /show_args
def show_args(request, a, b):
    return HttpResponse(a + ":" + b)


# /show_kwargs
def show_kwargs(request, id1, id2):
    return HttpResponse(id1 + ":" + id2)


# /test_redirect
def test_redirect(request):
    """使用反向解析重定向"""

    # 重定向到/index, 获取动态生成的url
    # url = reverse('booktest:index')

    # 重定向到show_args/1/2
    # url = reverse('booktest:show_args', args=(1, 2))

    # 重定向到show_kwargs/3/4
    url = reverse('booktest:show_kwargs', kwargs={"id1": 3, "id2": 4})

    # 跳转
    return redirect(url)
