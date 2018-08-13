from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

def index(request):
    """
    首页
    :param request:
    :return:
    """
    #查出没有删除的文章列表
    articles = Article.objects.filter(delflag=0).order_by('-create_time')
    paginator = Paginator(articles,1)
    page = request.GET.get('page', 1)
    try:
        current_page = paginator.page(page)
        contacts = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        contacts = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(1)
        contacts = current_page.object_list

    print(contacts)
    return render(request,'blog/index.html',{'contacts':contacts,'page':current_page})


def article_detail(request,article_id):
    article = Article.objects.get(id=article_id)
    return render(request,'blog/article_detail.html',{"article":article})