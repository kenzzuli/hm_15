from django.shortcuts import render, redirect  # 导入重定向函数
from booktest.models import BookInfo, HeroInfo, AreaInfo
from django.http import HttpResponseRedirect
from datetime import date


# Create your views here.

def index(request):
    # 查询出所有图书的信息
    book_list = BookInfo.objects.all()
    book_list = [i for i in book_list if not i.isDelete]
    # 使用模板
    return render(request, 'booktest/index.html',
                  {'book_list': book_list})


def create(request):
    """新增一本图书"""
    # 1.创建BookInfo对象
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1999, 9, 9)
    # 2.保存至数据库
    b.save()

    # return render(request, 'booktest/create.html', )

    # 返回应答，让浏览器再访问/index，重定向
    # return HttpResponseRedirect('/index')
    return redirect('/index')


def delete(request, bid):
    """删除点击的图书"""
    # 1.通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 2.删除
    book.isDelete = True
    book.save()

    # return render(request, 'booktest/delete.html',
    #               {'book': book})
    # 3.重定向
    # return HttpResponseRedirect('/index')
    return redirect('/index')


def areas(request):
    """显示地区"""
    # 1.当前地区
    area = AreaInfo.objects.get(atitle='广州市')
    # 2.子级地区 由一查多 一类对象.多类名小写_set.all()
    children_area = area.areainfo_set.all()
    # child_area = AreaInfo.objects.filter(aParent__atitle='广州市')
    # 3.父级地区 由多查一 多类对象.关联属性
    parent_area = area.aParent
    # 3.使用模板
    return render(request, 'booktest/areas.html',
                  {'area': area, 'children_area': children_area, 'parent_area': parent_area})
