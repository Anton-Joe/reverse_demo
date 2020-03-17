from django.http import  HttpResponse
from django.shortcuts import reverse, redirect


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('首页')
    else:
        # login_url = reverse('login')
        # return redirect(login_url)
        # kwarys : keyword arguments
        detail_url = reverse('detail', kwargs={'article_id': 1})
        return redirect(detail_url)


def login(request):
    return HttpResponse('登录页面')


def article(request, article_id):
    text = "您的文章id是%s" % article_id
    return HttpResponse(text)


