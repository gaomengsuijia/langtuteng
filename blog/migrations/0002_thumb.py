# Generated by Django 2.1 on 2018-08-17 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb_time', models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumb_article', to='blog.Article', verbose_name='点赞的文章')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumb_user', to=settings.AUTH_USER_MODEL, verbose_name='点赞人')),
            ],
            options={
                'verbose_name': '点赞',
                'verbose_name_plural': '点赞',
            },
        ),
    ]
