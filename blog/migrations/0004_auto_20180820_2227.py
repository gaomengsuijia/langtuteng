# Generated by Django 2.1 on 2018-08-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_del',
            field=models.CharField(default=0, max_length=4, verbose_name='删除标志'),
        ),
    ]
