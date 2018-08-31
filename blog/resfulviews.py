# -*- coding: utf-8 -*-
__author__ = "hulinjun"
from rest_framework import mixins,viewsets
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class ArticleListPagination(PageNumberPagination):
    """
    文章列表分页
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30
    page_query_param = 'page'



class ArticleListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    文章列表
    """
    queryset = Article.objects.filter(delflag=0)
    serializer_class = ArticleSerializer
    pagination_class = ArticleListPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    ordering = ('-create_time',)  # 默认倒序
    search_fields = ('title', 'summary')
