from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),  # 首页
    # url(r'^showarg(\d+)$', views.show_arg),  # 捕获url参数，位置参数
    url(r'^showarg(?P<arg>\d+)', views.show_arg),  # 捕获url参数，关键字参数
    url(r'^login$', views.login),  # 用户登录
    url(r'^login_check$', views.login_check),  # 用户登录校验
    url(r'^test_ajax$', views.test_ajax),  # 显示ajax页面
    url(r'^ajax_handle$', views.ajax_handle),  # 处理ajax
    url(r'^login_ajax$', views.login_ajax),  # ajax登录页面
    url(r'^login_check_ajax$', views.login_check_ajax),  # ajax登录校验
    url(r'^set_cookies$', views.set_cookies),  # 设置cookie信息
    url(r'^get_cookies$', views.get_cookies),  # 读取cookie信息
    url(r'^set_session$', views.set_session),  # 设置session
    url(r'^get_session$', views.get_session),  # 读取session
    url(r'^clear_session$', views.clear_session),  # 清除session
    url(r'^flush_session$', views.flush_session),  # 清空session
]
