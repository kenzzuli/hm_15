from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def set_session(request):
    """设置session"""
    request.session['username'] = 'ken'
    request.session['age'] = 18

    return HttpResponse('设置session')


def get_session(request):
    """获取session"""
    # session存储的是什么数据格式，读取的也是相同的数据格式
    username = request.session.get('username')
    age = request.session.get('age')

    return HttpResponse(username + ":" + str(age))
