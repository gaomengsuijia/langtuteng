from django.shortcuts import render
from .models import Article,ArticleColumn,Thumb
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from langtuteng import settings
import redis
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.
#连接redis

reds = redis.Redis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)



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
    total_views = reds.incr('article:{}:views'.format(article_id))
    total_thumb = article.thumb_article.all().count()
    return render(request,'blog/article_detail.html',{"article":article,"total_views":total_views,
                  "total_thumb":total_thumb})


@csrf_exempt
@require_POST
@login_required(login_url="/account/login")
def thumb(request):
    """
    点赞
    :param request:
    :return:
    """
    if request.method == "POST":
        article_id = request.POST.get('article_id')
        user = request.user
        print(article_id,user)
        old_thumb = Thumb.objects.filter(article_id=article_id,person_id=user.id)
        if old_thumb:
            return JsonResponse({"code":20002})#已经点赞
        else:
            new_thumb = Thumb(article_id=article_id,person_id=user.id)
            new_thumb.save()
            #查出总的点赞数
            total_thumb = Thumb.objects.filter(article_id=article_id).count()
            return JsonResponse({"code":20001,"total_thumb":total_thumb})