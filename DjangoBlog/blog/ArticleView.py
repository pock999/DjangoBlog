# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render,redirect
from blog.models import User,Article,Category
from django.http import HttpResponse,JsonResponse 
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth

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
        context['message']= "請先登入"
        return render(request,'index.html',context)  #未登入轉回主頁

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
        context['message']= "請先登入"
        return render(request,'index.html',context)  #未登入轉回主頁

def post_article(request):
    print('fdsfsd')
    context = {}
    if request.session.get('is_login',None): #檢查session確定是否登入
        
        if request.method == 'POST':   #如果是 <write_article.html> 按發布鈕傳送
                
            acc = request.session.get('user_account')   # 從session取得帳號
            print(acc)
            art_type = request.POST['art_type'] #取得表單傳送的文章類型、標題、內容
            art_title = request.POST['title']
            art_content = request.POST['content']
            print(Category.objects.filter(name=art_type))
            article_tmp = Article.objects.create(content=art_content,title=art_title,category=Category.objects.get(name=art_type),account=User.objects.get(account=acc))
            article_tmp.save()    #將資料寫入資料庫
            context['message']= "發布完成"
            
    else:
        context['message']= "請先登入"
    
    return render(request,'index.html',context) 
def edit_page(request):
    context = {}
    if request.session.get('is_login',None): #檢查session確定是否登入
        if request.method == 'POST':   #如果是 <manage.html> 按發布鈕傳送
            acc = request.session.get('user_account') # 從session取得帳號
            art_id = art_type = request.POST['article_id'] # 取得文章流水號
            article = Article.objects.get(auto_increment_id = art_id)
            get_acc = article.account.account #從表單提交的帳號
            if get_acc == acc:
                context['user'] =request.session.get('user_name') 
                context['account'] = request.session.get('user_account')
                context['link1']='登出'
                context['link2']='管理'
                context['art_id']= art_id
                title_option = []
                category = Category.objects.all()
                for cc in category:
                    title_option.append(cc)
                context['title_option']=title_option
                context['ori_cate']=article.category.name
                context['ori_title']=article.title
                context['ori_content']=article.content

                return render(request,'edit.html',context)
            else:
                context['message'] = '請勿嘗試錯誤分正當行為!!!'
                return render(request,'manage.html',context)
    else:
        context['message']= "請先登入"
        return render(request,'index.html',context) #未登入轉回主頁

def update_edit(request):
    context = {}
    if request.session.get('is_login',None): #檢查session確定是否登入
        if request.method == 'POST':   #如果是 <write_article.html> 按發布鈕傳送
            acc = request.session.get('user_account')   # 從session取得帳號
            art_type = request.POST['art_type'] #取得表單傳送的文章類型、標題、內容
            art_title = request.POST['title']
            art_content = request.POST['content']
            article_id = request.POST['article_id']
            ori_article = Article.objects.get(auto_increment_id=article_id)
            if acc == ori_article.account.account:
                ori_article.content = art_content
                ori_article.title = art_title
                ori_article.category = Category.objects.get(name=art_type)
                ori_article.save()
                context['message']='更新成功'
            else:
                context['message']='請勿嘗試錯誤分正當行為!!!'
    else:
        context['message']= "請先登入"

    return render(request,'index.html',context)