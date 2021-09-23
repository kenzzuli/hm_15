from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from booktest.models import PicTest, AreaInfo
from django.core.paginator import Paginator

# Create your views here.
# ip地址黑名单
EXCLUDE_IPS = ["202.121.96.187"]


def blocked_ips(view_func):
    """ip黑名单装饰器"""

    def wrapper(request, *args, **kwargs):
        if request.META['REMOTE_ADDR'] in EXCLUDE_IPS:
            return HttpResponse("<h1>Forbidden</h1>")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper


# /index
# @blocked_ips
def index(request):
    """首页"""
    # 获取浏览器端的ip地址
    # user_ip = request.META['REMOTE_ADDR']
    # print(user_ip)
    # if user_ip in EXCLUDE_IPS:
    #     return HttpResponse('<h1>Forbidden</h1>')

    print('---index----')
    # num = "a" + 1
    return render(request, 'booktest/index.html')


# /static_test
# @blocked_ips
def static_test(request):
    """静态文件"""
    # print(settings.STATICFILES_FINDERS)
    # ('django.contrib.staticfiles.finders.FileSystemFinder',
    # 'django.contrib.staticfiles.finders.AppDirectoriesFinder')

    return render(request, 'booktest/static_test.html')


def upload_pic(request):
    """上传图片页面"""
    return render(request, 'booktest/upload_pic.html')


def upload_handle(request):
    """处理上传图片"""
    # 1.获取上传图片的处理对象
    f1 = request.FILES.get('pic')
    # print(type(f1))
    # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
    # <class 'django.core.files.uploadedfile.TemporaryUploadedFile'>
    # 2.创建一个文件
    fname = '%s/booktest/%s' % (settings.MEDIA_ROOT, f1.name)
    # 3.写入
    with open(fname, mode='wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    # 4.在数据库中保存上传记录
    pic_name = 'booktest/%s' % f1.name
    PicTest.objects.create(goods_pic=pic_name)
    # 5.返回响应
    return HttpResponse('上传成功')


def show_area(request, pIndex):
    """分页"""
    # 获取所有省级地区
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 分页，每页10条数据
    paginator = Paginator(areas, 10)
    # 如果当前没有传递页码，则默认是第一页
    if pIndex == "":
        pIndex = "1"
    # 类型转换
    pIndex = int(pIndex)
    # 获取第pIndex页的数据 Page类的实例对象
    current_page = paginator.page(pIndex)
    # 获取所有的页码信息
    plist = paginator.page_range
    # 将当前页码、当前页的数据、页码信息传递到模板中
    return render(request, 'booktest/show_area.html',
                  dict(pIndex=pIndex, current_page=current_page, plist=plist))


def areas(request):
    """省市区三级联动"""
    return render(request, 'booktest/areas.html')


def get_provinces(request):
    """获取所有省份的json数据"""
    # 获取所有省份的对象
    provinces = AreaInfo.objects.filter(aParent__isnull=True)
    # 对象无法直接序列化为json数据，需要从对象中取出数据 id，atitle
    province_list = list()
    for province in provinces:
        province_list.append((province.id, province.atitle))
    # 返回数据
    return JsonResponse({'data': province_list})


def get_sub_areas(request, id):
    """获取当前区域的子区域"""
    # 由一查多
    # area = AreaInfo.objects.get(id)
    # sub_areas = area.areainfo_set.all()
    # 关联查询
    sub_areas = AreaInfo.objects.filter(aParent_id=id)
    sub_area_list = list()
    for sub_area in sub_areas:
        sub_area_list.append((sub_area.id, sub_area.atitle))
    return JsonResponse({'data': sub_area_list})
