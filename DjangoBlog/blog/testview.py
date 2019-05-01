
from __future__ import unicode_literals 
from django.shortcuts import render,redirect
from blog.models import User,Article
from django.http import HttpResponse,JsonResponse 
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth

def testProjectAPI(request):
    Dict = {'attr1': '屬性一', 'att2': '屬性二'}
    # listt = 
    # return JsonResponse(Dict,json_dumps_params={'ensure_ascii':False}) ==>return jsom{} 
    return JsonResponse(Dict,safe=False) 
    # return json []

def apiPage(request):
    return render(request, 'apitest.html')

def test(request):
    return render(request, 'NewPost.html')