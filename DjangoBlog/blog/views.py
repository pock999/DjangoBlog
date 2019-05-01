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

    


def registerView(request):
    if request.session.get('is_login',None): #檢查session確定是否登入，不允許重複登入
        return redirect("/")  #若已登入則導向主頁
    if request.method == 'POST':   #如果是 <register.html> 按登入鈕傳送
        acc = request.POST['account']   #取得表單傳送的帳號、密碼
        pwd = make_password(request.POST['password'])
        # pwd = request.POST['password']
        name = request.POST['name']
        try:
            user = User.objects.get(account=acc)  #以 user 取得名稱為acc的資料
        except:
            user = None   #若acc不存在則設定為 None
        if user != None:
            message = user.account + " 帳號已經建立! "
            print(message)
            return HttpResponse(message)
        else:  #建立 acc 帳號
            user = User.objects.create(account=acc,password=pwd,username=name)
            user.save()    #將資料寫入資料庫
            return redirect('/')   #若成功建立，重新導向至 index介面
    return render(request,"register.html",locals())  #註冊失敗則重導回<register.html>


def loginView(request):
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
                message = "登入成功"
                return redirect('/')
            else:
                message = "密碼不正確"
        except:
            message="該用戶不存在"
        
        print(message)
    return render(request,"login.html",locals())  #登入失敗則重導回<login.html>
# Create your views here.


def logoutView(request):
    if not request.session.get('is_login',None): #如果原本未登入，就不需要登出
        return redirect('/') 
    else:
        request.session.flush() #一次性將session內容全部清除
    return redirect('/') 

def manage_page(request):
    context = {}
    if request.session.get('is_login',None):
        context['user'] =request.session.get('user_name') 
        context['link1']='登出'
        context['link2']='新增文章'
        acc = request.session.get('user_account') 
        #列出所有文章
        article_set = []
        print(acc)
        for a in Article.objects.filter(account__account__exact = acc):
            arti = a
            article_set.append(arti)
        context['article'] = article_set
        return render(request, 'manage.html', context)
    else:
        return redirect("/")

def write_article_page(request):
    if request.session.get('is_login',None): #檢查session確定是否登入
        context = {}
        context['user'] =request.session.get('user_name') 
        context['account'] = request.session.get('user_account')
        context['link1']='登出'
        context['link2']='管理'
        title_option = []
        category = Category.objects.all()
        for cc in category:
            title_option.append(cc)
        context['title_option']=title_option
        return render(request,'write_article.html',context)
    else:
        return redirect("/") #未登入轉回主頁

def post_article(request):
    print('fdsfsd')
    if request.session.get('is_login',None): #檢查session確定是否登入
        
        if request.method == 'POST':   #如果是 <write_article.html> 按發布鈕傳送
                
                acc = request.POST['account']   #取得表單傳送的帳號、文章類型、標題、內容
                print(acc)
                art_type = request.POST['art_type']
                art_title = request.POST['title']
                art_content = request.POST['content']
                print(Category.objects.filter(name=art_type))
                article_tmp = Article.objects.create(content=art_content,title=art_title,category=Category.objects.get(name=art_type),account=User.objects.get(account=acc))
                article_tmp.save()    #將資料寫入資料庫
                return redirect("/")
    else:
        return redirect("/") #未登入轉回主頁

def notFoundPage(request):
    return render(request, '404.html')

def errorServer(request):
    return render(request, '500.html')