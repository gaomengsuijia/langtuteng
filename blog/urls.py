# -*- coding: utf-8 -*-
__author__ = "langtuteng" 
from django.urls import path,include
from . import views
from rest_framework import routers
from .resfulviews import ArticleListViewSet
router = routers.DefaultRouter()
router.register(r'articles', ArticleListViewSet,base_name="articles")


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>', views.article_detail,name='article'),
    path('thumb', views.thumb, name='thumb'),
    path('comment', views.comment, name='comment'),
    path('api/',include(router.urls)),
    path('search',views.article_search,name='search'),
    path('columnlist/<int:column_id>',views.columnlist,name='columnlist')
]
