"""test12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from app1 import views

app_name='app1'

urlpatterns = [
      path('', views.Home.as_view(),name='home'),
      path('register/', views.register,name='register'),
      path('login/', views.login1,name='login'),
      path('logout/', views.logout1,name='logout'),
      path('profile/', views.Detail.as_view(),name='profile'),
     path('userprofiles/', views.userlist,name='userprofiles'),

]
