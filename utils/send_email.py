# -*- coding: utf-8 -*-
__author__ = "hulinjun"
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import string
import random
from django.urls import reverse
from account.models import Emailactivecode

class Sendemail(object):
    """
    发送邮件
    """
    def __init__(self,sendtype):
        self.sendtype = sendtype


    def send(self,to_email):
        """
        发送
        :return:
        """
        if self.sendtype=='forgetpassword':
            email_code = self.gene_email_code()
            from_email = settings.DEFAULT_FROM_EMAIL
            subject = '狼图腾博客密码找回,请勿回复'
            url_tl = settings.URLTL
            html_content = url_tl.format(email_code)
            msg = EmailMultiAlternatives(subject, html_content,from_email, [to_email])
            msg.content_subtype='html'
            try:
                msg.send()
                emailactivecode = Emailactivecode()
                emailactivecode.email = to_email
                emailactivecode.email_code = email_code
                emailactivecode.send_type = self.sendtype
                emailactivecode.is_delete = 0
                emailactivecode.save()
            except Exception:
                raise Exception("邮箱发送失败")
            print('发送成功')



    def gene_email_code(self,link_code_length=16):
        """
        生成邮件链接的重置密码的code
        :return:
        """
        """生成随机邮箱验证码，作为验证链接的一部分"""
        chars = string.ascii_letters + str(string.digits)
        link_code = ''.join([random.choice(chars) for i in range(link_code_length)])
        return link_code




if __name__ == '__main__':
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "langtuteng.settings")  # 在Django 里想单独执行文件写上这句话
    import django  # 导入Django
    django.setup()
    sendemail = Sendemail(sendtype='forgetpassword')
    # code = sendemail.gene_email_code()
    # print(code)
    urls = reverse('account:forgetpassword')
    print(urls)
    # sendemail.send('hulinjun2006@126.com')
