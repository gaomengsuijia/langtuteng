# -*- coding: utf-8 -*-
__author__ = "langtuteng" 
from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),
    path('myself', views.myself, name='myself'),
    path('userinfo', views.userinfo, name='userinfo'),
    path('modifypassword', views.modifypassword, name='modifypassword'),
    path('my_image',views.my_image,name='my_image'),
    path('forgetpassword',views.Forgetpassword.as_view(),name='forgetpassword'),
    path('resetpassword/<str:email_code>/',views.Resetpassword.as_view(),name='resetpassword'),
]