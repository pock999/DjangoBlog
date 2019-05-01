"""DjangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import registerView,loginView,logoutView,index,notFoundPage,errorServer,manage_page,write_article_page,post_article
from blog.testview import apiPage,testProjectAPI,test
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="homepage"),
    path('login/',loginView,name="Login"),
    path('register/',registerView,name="Register"),
    path('logout/',logoutView,name="Logout"),
    path('404test/',notFoundPage),
    path('500test/',errorServer),
    path('manage/',manage_page,name="ManagePage"),
    path('testAPI/',testProjectAPI,name="testAPI"),
    path('apitest/',apiPage,name="api"),
    path('testNew/',test),
    path('manage/write_article/',write_article_page,name="Write_Article"),
    path('manage/write_article/post_article',post_article,name="Post_Article"),
]

hander404 = notFoundPage
hander500 = errorServer
#settings.py 的 DEBUG要變成False(表示非開發階段)
#ALLOWED_HOSTS = []要變成['*']
#錯誤頁面才會出現