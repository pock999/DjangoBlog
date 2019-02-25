from django.shortcuts import render,redirect
from blog.models import User
from django.http import HttpResponse
from django.contrib.auth.backends import ModelBackend
from django.contrib import auth
from django.db.models import Q

def index(request):
    context          = {}
    if request.session.get('is_login',None): #檢查session確定是否登入，不允許重複登入
        context['user'] =request.session.get('user_name') 
        context['href1']='logout'
        context['href2']='#'
        context['link1']='登出'
        context['link2']='管理'
    else:
        context['user'] =''
        context['href1']='login'
        context['href2']='register'
        context['link1']='登入'
        context['link2']='註冊'
    
    return render(request, 'index.html', context)

def home(request):
    context          = {}
    if request.session.get('is_login',None): #檢查session確定是否登入，不允許重複登入
        context['user'] =request.session.get('user_name') 
    else:
        context['user'] =''
    
    return render(request, 'index.html', context)
    
    
    

# def login_page(request):
#     return render(request, 'login.html')


def registerView(request):
    if request.session.get('is_login',None): #檢查session確定是否登入，不允許重複登入
        return redirect("/")  #若已登入則導向主頁
    if request.method == 'POST':   #如果是 <register.html> 按登入鈕傳送
        acc = request.POST['account']   #取得表單傳送的帳號、密碼
        pwd = request.POST['password']
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
            if user.password == pwd:
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
    request.session.flush() #一次性將session內容全部清除
    return redirect('/') 
    