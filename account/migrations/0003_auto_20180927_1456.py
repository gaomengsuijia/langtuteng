# Generated by Django 2.1 on 2018-09-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180927_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailactivecode',
            name='email_code',
            field=models.CharField(max_length=20, null=True, verbose_name='邮箱激活码'),
        ),
        migrations.AlterField(
            model_name='emailactivecode',
            name='send_type',
            field=models.CharField(max_length=40, null=True, verbose_name='邮件类型'),
        ),
    ]