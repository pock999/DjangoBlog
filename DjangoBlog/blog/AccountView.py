# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render,redirect
from blog.models import User,Article,Category
from django.http import HttpResponse,JsonResponse 
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth

def registerView(request):
    content = {}
    if request.session.get('is_login',None): #檢查session確定是否登入，不允許重複登入
        return redirect("/")  #若已登入則導向主頁
    if request.method == 'POST':   #如果是 <register.html> 按登入鈕傳送
        acc = request.POST['account']   #取得表單傳送的帳號、密碼
        pwd = make_password(request.POST['password'])
        # pwd = request.POST['password']
        name = request.POST['name']
        if name == '' or acc=='' or pwd =='':
            content['message'] = '任何一欄不得為空'
        else:
            try:
                user = User.objects.get(account=acc)  #以 user 取得名稱為acc的資料
            except:
                user = None   #若acc不存在則設定為 None
            
            if user != None:
                message = user.account + " 帳號已經建立! "
                print(message)
                content['message'] = message
            else:  #建立 acc 帳號
                user = User.objects.create(account=acc,password=pwd,username=name)
                user.save()    #將資料寫入資料庫
                content['message'] = '註冊成功'
                return render(request,'index.html',content)   #若成功建立，重新導向至 index介面   
           
    return render(request,"register.html",content)#註冊失敗則重導回<register.html>


def loginView(request):
    content = {}
    if request.session.get('is_login',None): #檢查session確定是否登入，不允許重複登入
        return redirect("/")  #若已登入則導向主頁
    if request.method == 'POST':   #如果是 <login.html> 按登入鈕傳送
        acc = request.POST['account']   #取得表單傳送的帳號、密碼
        pwd = request.POST['password']
        try:
            user = User.objects.get(account=acc)
            print('輸入:'+pwd)
            print('實際:'+user.password)
            # if user.password == pwd:
            if check_password(pwd,user.password):
                #使用session寫入登入者資料
                request.session['is_login'] = True
                request.session['user_account'] = user.account
                request.session['user_name'] = user.username
                content['message'] = "登入成功"
                return render(request,'index.html',content) 
            else:
                message = "密碼不正確"
        except:
            message="該用戶不存在"
        
        print(message)
        
        content['message'] = message
    return render(request,"login.html",content)  #登入失敗則重導回<login.html>
# Create your views here.


def logoutView(request):
    content = {}
    if not request.session.get('is_login',None): #如果原本未登入，就不需要登出
        content['message'] = '未登入帳號!!'
    else:
        request.session.flush() #一次性將session內容全部清除
        content['message'] = "登出成功"
    return render(request,'index.html',content) 