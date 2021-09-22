from django.conf.urls import url
from booktest import views

urlpatterns = [url(r'^$', views.index),  # 图书列表页
               url(r'^index$', views.index),  # 图书列表页
               url(r'^create$', views.create),  # 增加一本图书
               url(r'^delete/(\d+)$', views.delete),  # 删除一本图书
               url(r'^areas$', views.areas)  # 地区列表
               ]
