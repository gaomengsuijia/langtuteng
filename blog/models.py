from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ArticleColumn(models.Model):
    """
     文章栏目
    """
    user = models.ForeignKey(User,related_name="article_column",verbose_name="创建者",on_delete=models.CASCADE)
    column = models.CharField(max_length=50,verbose_name="栏目名称")
    create_time = models.DateField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateField(verbose_name="修改时间",blank=True,null=True)

    def __str__(self):
        return self.column

    class Meta:
        verbose_name = '文章栏目'
        verbose_name_plural = '文章栏目'


class Article(models.Model):
    """
    文章
    """
    author = models.ForeignKey(User,related_name="article",verbose_name="发表者",on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name="文章标题")
    column = models.ForeignKey('ArticleColumn',verbose_name="所属栏目",on_delete=models.CASCADE)
    body = models.TextField(verbose_name="文章详情")
    create_time = models.DateField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateField(verbose_name="修改时间",blank=True,null=True)
    delflag = models.CharField(verbose_name="删除标志",default=0,max_length=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"