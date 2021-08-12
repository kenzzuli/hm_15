from django.contrib import admin
from django.urls import path
from booktest import views

urlpatterns = [
    path(r'set_session', views.set_session),
    path(r'get_session', views.get_session)
]
