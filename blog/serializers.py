# -*- coding: utf-8 -*-
__author__ = "hulinjun"
from rest_framework import serializers
from .models import Article,ArticleColumn

class ColumnSerializer(serializers.ModelSerializer):
    """
    文章分类
    """
    class Meta:
        model = ArticleColumn
        fields = ('column','id')


class ArticleSerializer(serializers.ModelSerializer):
    """
    文章序列化对象
    """
    column = ColumnSerializer()
    class Meta:
        model = Article
        fields = ('id','title','summary','column','create_time')