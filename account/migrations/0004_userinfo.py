# Generated by Django 2.1 on 2018-09-01 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_auto_20180901_0912'),
    ]

    operations = [
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
