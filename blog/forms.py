# -*- coding: utf-8 -*-
__author__ = "langtuteng"
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content','com_article')
