# -*- coding: utf-8 -*-
__author__ = "hulinjun"
from django import forms
from .models import Account
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    """
    登录表单
    """
    username = forms.CharField()
    password = forms.CharField()



class RegisterForm(forms.ModelForm):
    """
    注册表单
    """
    password = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']


class AcountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('nickname','phone')