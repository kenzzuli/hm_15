# 定义视图函数
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo, HeroInfo  # 导入图书模型类，英雄模型类


def my_render(request, template_path, context_dict={}):
    """使用模板文件的封装，这其实就是上面导入的render函数"""
    # 1. 加载模板文件，获取模板对象
    temp = loader.get_template(template_path)
    # 2. 定义模板上下文，给模板文件传数据
    context = RequestContext(request, context_dict)
    # 3. 模板渲染，产生标准的html内容
    res_html = temp.render(context)
    # 4. 返回给浏览器
    return HttpResponse(res_html)


# Create your views here.
# 1.定义视图函数
# 2.进行url配置，建立url地址和视图的对应关系

#  用户请求http://127.0.0.1:8000/index时调用该函数
def index(request):
    """
    :param request: HttpRequest对象
    :return:
    """
    # 进行处理，和M和T进行交互
    # return HttpResponse("老铁，没毛病")

    # # 使用模板文件
    # # 1. 加载模板文件，获取模板对象
    # temp = loader.get_template('booktest/index.html')  # 该路径是相对于settings.py中TEMPLATES DIR的
    # # 2. 定义模板上下文，给模板文件传数据
    # context = RequestContext(request, {})
    # # 3. 模板渲染，产生标准的html内容
    # res_html = temp.render(context)
    # # 4. 返回给浏览器
    # return HttpResponse(res_html)

    # 对上述过程可以进行封装
    # return my_render(request, 'booktest/index.html')

    # 使用Django封装好的render函数
    return render(request, 'booktest/index.html',
                  {'content': 'hello world',
                   'list': list(range(1, 10))},
                  )


def index2(request):
    return HttpResponse("hello world")


def show_books(request):
    """显示图书列表页"""
    # 1.通过M查找图书表中的数据
    book_list = BookInfo.objects.all()
    # 2.使用模板
    return render(request, 'booktest/show_books.html',
                  {'book_list': book_list})


def detail(request, id):
    """
    查询图书关联的英雄信息
    :param request:
    :param id: 正则分组的结果
    """
    # print(type(id))  # str
    # 1. 根据id查询图书信息
    book = BookInfo.objects.get(id=id)
    # 2. 查询和book相关联的影响信息
    hero_list = book.heroinfo_set.all()
    # 3. 使用模板
    return render(request, 'booktest/detail.html',
                  {'book': book,
                   'hero_list': hero_list,
                   })
