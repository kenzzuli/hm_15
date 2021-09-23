from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^set_session$', views.set_session),  # 设置session
    url(r'^get_session$', views.get_session),  # 获取session
]
