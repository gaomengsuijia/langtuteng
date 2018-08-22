from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    """
    用户
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20,verbose_name="昵称")
    phone = models.CharField(max_length=12,verbose_name="手机号码",blank=True)

    class Meta:
        verbose_name = "注册用户"
        verbose_name_plural = "注册用户"