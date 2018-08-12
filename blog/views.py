from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    return render(request,'blog/index.html')


def article_detail(request,article_id):
    article = Article.objects.get(id=article_id)
    return render(request,'blog/article_detail.html',{"article":article})