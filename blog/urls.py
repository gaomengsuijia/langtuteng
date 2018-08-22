# -*- coding: utf-8 -*-
__author__ = "langtuteng" 
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>', views.article_detail,name='article'),
    path('thumb', views.thumb, name='thumb'),
    path('comment', views.comment, name='comment'),
]