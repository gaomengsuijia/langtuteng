from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    """
    用户
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="account_user")
    nickname = models.CharField(max_length=20,verbose_name="昵称")
    phone = models.CharField(max_length=12,verbose_name="手机号码",blank=True)

    class Meta:
        verbose_name = "注册用户"
        verbose_name_plural = "注册用户"


class Userinfo(models.Model):
    """
    用户的详细资料
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="userinfo_user")
    photo = models.ImageField(upload_to='myself/phone')
    address = models.CharField(max_length=100,verbose_name="地址",blank=True)
    company = models.CharField(max_length=100,verbose_name="学校",blank=True)
    profession = models.CharField(max_length=100,verbose_name="职业",blank=True)
    aboutme = models.TextField(verbose_name="个人简介",blank=True)

    def __str__(self):
        return "user:{}".format(self.user.username)
