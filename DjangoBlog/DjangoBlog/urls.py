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
from blog.views import registerView,loginView,logoutView,index,notFoundPage,errorServer,manage_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('login/',loginView),
    path('register/',registerView),
    path('logout/',logoutView),
    path('404test/',notFoundPage),
    path('500test/',errorServer),
    path('manage/',manage_page),
    path('manage/logout/',logoutView),
]

hander404 = notFoundPage
hander500 = errorServer
#settings.py 的 DEBUG要變成False(表示非開發階段)
#ALLOWED_HOSTS = []要變成['*']
#錯誤頁面才會出現