# Generated by Django 2.1 on 2018-12-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookviews',
            name='views_num',
            field=models.IntegerField(default=0, verbose_name='浏览量'),
        ),
    ]
