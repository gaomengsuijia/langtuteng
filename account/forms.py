# -*- coding: utf-8 -*-
__author__ = "hulinjun"
from django import forms
from .models import Account
from django.contrib.auth.models import User
import re
from django.core.exceptions import ValidationError


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


    def clean(self):
        """
        验证字段
        :return:
        """
        cleaned_data = self.cleaned_data
        username_re = re.compile(r'^[a-zA-Z]{5,10}$')
        email_re = re.compile(r'.+@.+\.[a-zA-Z]{2,4}$')
        password_re = re.compile(r'^[0-9a-zA-Z]{6,15}$')
        username = cleaned_data['username']
        email = cleaned_data['email']
        password = cleaned_data['password']
        if(re.findall(username_re,username) and re.findall(email_re,email) and re.findall(password_re,password)):
            return cleaned_data
        else:
            raise ValidationError("user 参数不符合格式")



class AcountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('nickname','phone')



    def clean(self):
        """
        验证nickname,phone
        :return:
        """
        cleaned_data = self.cleaned_data
        nickname_re = re.compile(r'[^~#^$@%&!*()<>:;\'\"{}【】  ]')
        phone_re = re.compile(r'^[1][3,4,5,7,8][0-9]{9}$')
        nickname = cleaned_data['nickname']
        phone = cleaned_data['phone']
        if (re.findall(nickname_re,nickname) and re.findall(phone_re,phone)):
            return cleaned_data
        else:
            raise ValidationError("account 字段格式不对")