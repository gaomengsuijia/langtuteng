# Generated by Django 2.1 on 2018-09-27 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('phone', models.CharField(blank=True, max_length=12, verbose_name='手机号码')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '注册用户',
                'verbose_name_plural': '注册用户',
            },
        ),
        migrations.CreateModel(
            name='Emailactivecode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='发送的邮箱')),
                ('email_code', models.CharField(blank=True, max_length=10, verbose_name='邮箱激活码')),
                ('is_delete', models.CharField(blank=True, default=0, max_length=2, verbose_name='是否已经使用')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('send_type', models.CharField(blank=True, max_length=20, verbose_name='邮件类型')),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myself/phone')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='地址')),
                ('company', models.CharField(blank=True, max_length=100, verbose_name='学校')),
                ('profession', models.CharField(blank=True, max_length=100, verbose_name='职业')),
                ('aboutme', models.TextField(blank=True, verbose_name='个人简介')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userinfo_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
