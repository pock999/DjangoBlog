# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render,redirect
from blog.models import User,Article,Category
from django.http import HttpResponse,JsonResponse 
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth


def index(request):
    context          = {}
    if request.session.get('is_login',None): #檢查session確定是否登入，不允許重複登入
        context['user'] =request.session.get('user_name') 
        context['link1']='登出'
        context['link2']='管理'
    else:
        context['user'] =''
        context['link1']='登入'
        context['link2']='註冊'
    
    #列出所有文章
    article_set = []
    
    for a in Article.objects.all():
        arti = a
        article_set.append(arti)
    
    context['article'] = article_set
    return render(request, 'index.html', context)

    




def notFoundPage(request):
    return render(request, '404.html')

def errorServer(request):
    return render(request, '500.html')