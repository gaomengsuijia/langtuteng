from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ArticleColumn(models.Model):
    """
     文章栏目
    """
    user = models.ForeignKey(User,related_name="article_column",verbose_name="创建者",on_delete=models.CASCADE)
    column = models.CharField(max_length=50,verbose_name="栏目名称")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(verbose_name="修改时间",blank=True,null=True)

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
    summary = models.TextField(max_length=200,verbose_name="文章概要")
    column = models.ForeignKey('ArticleColumn',verbose_name="所属栏目",on_delete=models.CASCADE,related_name='articles')
    body = models.TextField(verbose_name="文章详情")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(verbose_name="修改时间",blank=True,null=True)
    delflag = models.CharField(verbose_name="删除标志",default=0,max_length=2)
    views_num = models.IntegerField(verbose_name="浏览量", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"



class Thumb(models.Model):
    """
    点赞
    """
    article = models.ForeignKey(Article,related_name='thumb_article',verbose_name="点赞的文章",on_delete=models.CASCADE)
    person = models.ForeignKey(User,related_name='thumb_user',verbose_name="点赞人",on_delete=models.CASCADE)
    thumb_time = models.DateTimeField(verbose_name="点赞时间",auto_now_add=True)

    def __str__(self):
        return 'article:{} person:{}'.format(self.article,self.person)


    class Meta:
        verbose_name="点赞"
        verbose_name_plural = "点赞"


class Comment(models.Model):
    """
    评论
    """
    content = models.TextField(verbose_name="评论内容")
    com_person = models.ForeignKey(User,verbose_name="评论人",related_name="per_comment",on_delete=models.CASCADE)
    com_article = models.ForeignKey(Article,verbose_name="评论的文章",related_name="art_comment",on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    is_del = models.CharField(verbose_name="删除标志",max_length=4,default=0)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'



class Book(models.Model):
    """
    电子书
    """
    bookname = models.CharField(verbose_name="书名",max_length=50)
    author = models.CharField(verbose_name="作者",max_length=50)
    catory = models.CharField(verbose_name="分类",max_length=50)
    doubanscore = models.CharField(verbose_name="豆瓣评分",max_length=50)
    about = models.TextField(verbose_name="简介",max_length=500)
    baidudiskurl = models.URLField(verbose_name="百度下载地址",blank=True)
    views = models.CharField(verbose_name="浏览量",blank=True,max_length=20)

    def __str__(self):
        return self.bookname

    class Meta:
        verbose_name = "电子书"
        verbose_name_plural = "电子书"
