# -*- coding: utf-8 -*-
__author__ = "hulinjun"
from django import forms
from .models import Account,Userinfo
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
        if email:
            if (re.findall(username_re, username) and re.findall(email_re, email) and re.findall(password_re,password)):
                return cleaned_data
            else:
                raise ValidationError("user 参数不符合格式")

        else:
            if (re.findall(username_re, username) and re.findall(password_re,password)):
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
        nickname = cleaned_data.get('nickname','')
        phone = cleaned_data['phone']
        if not nickname:
            self.add_error('nickname', '请输入正确格式的昵称')
            return None
        if phone:
            if (re.findall(nickname_re,nickname) and re.findall(phone_re,phone)):
                return cleaned_data
            else:
                if not re.findall(nickname_re,nickname):
                    self.add_error('nickname','请输入正确格式的昵称')
                    return None
                elif not re.findall(phone_re,phone):
                    self.add_error('phone','请输入正确格式的电话号码')
                    return None
                else:
                    raise ValidationError("account 字段格式不对")
        else:
            if re.findall(nickname_re,nickname):
                return cleaned_data
            else:
                self.add_error('nickname','请输入正确格式的昵称')
                return None



class UserinfoForm(forms.ModelForm):
    """
    用户详细资料
    """
    class Meta:
        model = Userinfo
        fields = ('address','company','profession','aboutme')


class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class ChangepasswordForm(forms.Form):
    """
    修改密码
    """
    new_password = forms.CharField(max_length=30)
    confirm_new_password = forms.CharField(max_length=30)


    def clean_confirm_new_password(self):
        cd = self.cleaned_data
        if cd['new_password'] != cd['confirm_new_password']:
            self.add_error('confirm_new_password', "两次密码不一致")
            return None
        return cd['confirm_new_password']


    def clean(self):
        clean_data = self.cleaned_data
        password_re = re.compile(r'^[0-9a-zA-Z]{6,15}$')
        new_password = clean_data.get('new_password','')
        if re.findall(password_re,new_password):
            return clean_data
        else:
            self.add_error('new_password',"密码格式不正确")
            return None
