from django.shortcuts import render
from .models import Article,ArticleColumn
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

def index(request):
    """
    首页
    :param request:
    :return:
    """
    #查出所有的文章分类以及每个类目下的文章总数
    articlecolumn = ArticleColumn.objects.all()
    column_data = []
    for each in articlecolumn:
        dic = {
            'id':each.id,
            'name':each.column,
            'num':len(each.articles.filter(delflag=0))
        }
        column_data.append(dic)
    #查出没有删除的文章列表
    articles = Article.objects.filter(delflag=0).order_by('-create_time')
    paginator = Paginator(articles,10)
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

    return render(request,'blog/index.html',{'contacts':contacts,'page':current_page,'column_data':column_data})


def article_detail(request,article_id):
    article = Article.objects.get(id=article_id)
    return render(request,'blog/article_detail.html',{"article":article})