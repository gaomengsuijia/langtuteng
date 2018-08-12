from django.contrib import admin

# Register your models here.

from .models import Article,ArticleColumn


class ArticleAdmin(admin.ModelAdmin):

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all.js',  # 这是在后台的页面中追加js文件
            '/static/js/kindeditor/lang/zh-CN.js',
            '/static/js/kindeditor/config.js',
        )


admin.site.register(Article, ArticleAdmin)

class ArticleColumnAdmin(admin.ModelAdmin):
    pass

admin.site.register(ArticleColumn,ArticleColumnAdmin)