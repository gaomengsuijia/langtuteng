# -*- coding: utf-8 -*-
__author__ = "hulinjun"
from django import forms


class LoginForm(forms.Form):
    """
    登录表单
    """
    username = forms.CharField()
    password = forms.CharField()