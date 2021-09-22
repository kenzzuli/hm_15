from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^index2$', views.index2),  # 模板文件加载顺序
    url(r'^tem_var$', views.tem_var),  # 模板变量
    url(r'^tem_tag$', views.tem_tag),  # 模板标签
    url(r'^tem_filter$', views.tem_filter),  # 模板过滤器
    url(r'^tem_inherit$', views.tem_inherit),  # 模板继承
    url(r'^html_escape$', views.html_escape),  # html转义
    url(r'^login$', views.login),  # 登录页面
    url(r'^login_check$', views.login_check),  # 登录校验页面
    url(r'^change_pwd$', views.change_pwd),  # 修改密码页面
    url(r'^change_pwd_action$', views.change_pwd_action),  # 处理修改密码页面
    url(r'^verify_code$', views.verify_code),  # 生成验证码图片
    url(r'^verify_show$', views.verify_show),  # 显示验证页面
    url(r'^verify_yz$', views.verify_yz),  # 验证用户提交的验证码

]
