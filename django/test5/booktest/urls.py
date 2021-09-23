from django.conf.urls import url
from booktest import views

urlpatterns = [
    url('^index$', views.index),  # 首页
    url(r'^static_test$', views.static_test),  # 静态文件显示
    url(r'^upload_pic$', views.upload_pic),  # 上传图片页面
    url(r'^upload_handle$', views.upload_handle),  # 处理上传图片
    url(r'^show_area(\d*)$', views.show_area),  # 分页
    url(r'^areas$', views.areas),  # 省市区三级联动
    url(r'^get_provinces$', views.get_provinces),  # 获取省级数据
    url(r'^get_sub_areas(\d+)$', views.get_sub_areas),  # 获取下级区域
]
