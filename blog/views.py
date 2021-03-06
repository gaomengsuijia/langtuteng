from django.shortcuts import render,HttpResponseRedirect,render_to_response
from .models import Article,ArticleColumn,Thumb,Comment,Book
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.urls import reverse
import requests
import json
# Create your views here.

def page_not_found(request):
    """
    404错误
    :param request:
    :return:
    """
    return render_to_response('blog/404.html')

def page_error(request):
    """
    500错误
    :param request:
    :return:
    """
    return render_to_response('blog/500.html')

def index(request):
    """
    首页
    :param request:
    :return:
    """
    #查出阅读量前5的文章
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
    #查出阅读排行top5的文章
    top_rank = articles.order_by('-views_num')[:5]

    try:
        current_page = paginator.page(page)
        contacts = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        contacts = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(1)
        contacts = current_page.object_list

    return render(request,'blog/index.html',{'contacts':contacts,'page':current_page,'column_data':column_data,
                                             'top_rank':top_rank})


def article_detail(request,article_id):
    try:
        article = Article.objects.get(id=article_id)
        #浏览量+1
        article.views_num += 1
        article.save()
        total_views = article.views_num
        #查出总的点赞数
        total_thumb = article.thumb_article.all().count()
        #查出所有的评论数
        all_comment = article.art_comment.filter(is_del=0).order_by('-create_time')
        return render(request,'blog/article_detail.html',{"article":article,"total_views":total_views,
                      "total_thumb":total_thumb,"all_comment":all_comment})
    except Article.DoesNotExist as e:
        return HttpResponseRedirect(reverse('blog:index'))


@csrf_exempt
@require_POST
def thumb(request):
    """
    点赞
    :param request:
    :return:
    """
    if request.method == "POST":
        if request.user.is_authenticated:
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
        else:
            return JsonResponse({"code":20004})

@require_POST
def comment(request):
    """
    评论
    :param request:
    :return:
    """
    if request.method == "POST":
        comment_html = """
        <div class="reply_item">
          <div class="infos">
            <div class="info">
              <span class="name">
                <a class="user-name" data-name="Meteorix" href="/Meteorix">{0}</a>
              </span>
              <span class="sub-info">
                <a class="time" href="#reply-117734"><abbr class="timeago" title="" rel="twipsy" data-original-title="2018年08月13日">{1}</abbr></a>
              </span>
        
              <span class="opts  pull-right">
                  <span class="hideable">
                      <a data-toggle="tooltip"  href="?order_by=created_at&amp;#replies"><i class="glyphicon glyphicon-remove"></i></a>
                 </span>
              </span>
            </div>
        
            <div class="markdown">
              <p>{2}</p>
            </div>
          </div>
        
        </div>
        """
        if request.user.is_authenticated:#未登陆
            article_id = request.POST['articleid']
            comment = request.POST['replybody']
            user = request.user
            article = Article.objects.filter(id=article_id)
            if comment == '' or len(comment) > 200:
                return JsonResponse({"code":20003})#内容为空或大于200长度，不保存
            if article:
                new_comment = Comment(com_article_id=article_id,com_person_id=user.id,content=comment)
                new_comment.save()
                #将创建时间格式化
                create_time = new_comment.create_time.strftime('%Y-%m-%d %H:%M:%S')
                comment_html = comment_html.format(user,create_time,comment)
                return JsonResponse({"code":20001,"comment_html":comment_html})
            else:
                return JsonResponse({"code":20002})#文章不存在
        else:
            return JsonResponse({"code":20004})


def article_search(request):
    """
    文章搜索
    :param request:
    :return:
    """
    if request.method == "GET":
        keyword = request.GET.get('keyword','')
        if keyword:
            queryset = Article.objects.filter(Q(title__icontains=keyword) | Q(summary__icontains=keyword),delflag=0)
            paginator = Paginator(queryset,10)
            page = request.GET.get('page',1)

            try:
                current_page = paginator.page(page)
                contacts = current_page.object_list
            except PageNotAnInteger:
                current_page = paginator.page(1)
                contacts = current_page.object_list
            except EmptyPage:
                current_page = paginator.page(1)
                contacts = current_page.object_list

            return render(request,'blog/search.html',{'contacts':contacts,'page':current_page,'keyword':keyword})
        else:
            return HttpResponseRedirect(reverse('blog:index'))

    else:
        return HttpResponseRedirect(reverse('blog:index'))



def columnlist(request,column_id):
    """
    分类列表页面
    :param request:
    :return:
    """
    # 查出阅读量前5的文章
    # 查出所有的文章分类以及每个类目下的文章总数
    if column_id:
        current_columm = ArticleColumn.objects.filter(id=column_id)
        if not current_columm:
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            articlecolumn = ArticleColumn.objects.all()
            column_data = []
            for each in articlecolumn:
                dic = {
                    'id': each.id,
                    'name': each.column,
                    'num': len(each.articles.filter(delflag=0))
                }
                column_data.append(dic)
            # 查出没有删除的文章列表
            articles = Article.objects.filter(delflag=0,column=column_id).order_by('-create_time')
            paginator = Paginator(articles, 10)
            page = request.GET.get('page', 1)
            # 查出阅读排行top5的文章
            top_rank = articles.order_by('-views_num')[:5]
            try:
                current_page = paginator.page(page)
                contacts = current_page.object_list
            except PageNotAnInteger:
                current_page = paginator.page(1)
                contacts = current_page.object_list
            except EmptyPage:
                current_page = paginator.page(1)
                contacts = current_page.object_list

            return render(request, 'blog/column_list.html', {'contacts': contacts, 'page': current_page, 'column_data': column_data,
                                                       'top_rank': top_rank,"current_columm":current_columm[0].column})



def suibi(request):
    """
    随笔
    :param request:
    :return:
    """
    books = Book.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(books,20)
    try:
        current_page = paginator.page(page)
        contracts = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        contracts = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(1)
        contracts = current_page.object_list


    return render(request,'blog/suibi.html',{'books':contracts,'page':current_page})


def bookdetail(request,book_id):
    """
    书籍详情
    :param request:
    :param book_id:
    :return:
    """
    try:
        book = Book.objects.get(id=book_id)
        #添加浏览量
        book.views = str(int(book.views if book.views else 0) + 1)
        book.save()
        return render(request,'blog/bookdetail.html',{'book':book})
    except Book.DoesNotExist as e:
        return HttpResponseRedirect(reverse('blog:index'))



def book_search(request):
    """
    书籍搜索
    :param request:
    :return:
    """
    keyword = request.GET.get('keyword','')
    if keyword.strip() == '':
        return HttpResponseRedirect(reverse("blog:index"))
    books = Book.objects.filter(Q(bookname__contains=keyword)|Q(author__contains=keyword))
    return render(request,'blog/searchbook.html',{'books':books,'keyword':keyword})



def movie(request):
    """
    获取猫扑上的电影票房
    :param request:
    :return:
    """
    data = {}
    try:
        res = requests.get(url="https://box.maoyan.com/promovie/api/box/second.json").text
        data = json.loads(res)
    except Exception as e:
        print("数据获取失败")
    return render(request, 'blog/movie.html', {"data": data})
