from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.views.generic import View,ListView,DetailView
from .models import *
from comments.forms import CommentForm
from comments.models import Comment
from django.core.paginator import Paginator
import markdown
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
# Create your views here.

class IndexView(View):
    def get(self,req):
        articles = Article.objects.all()
        # newarticle = articles.order_by("-create_time")[:3]   老办法,需要每个页面都添加out
        paginator = Paginator(articles, 2)
        # print(paginator.count)
        # print(paginator.object_list)
        # print(paginator.allow_empty_first_page)
        # print(paginator.get_page(2))

        # print(paginator.page_range)
        pagennum = req.GET.get("page")
        pagennum = 1 if pagennum == None else pagennum
        page = paginator.get_page(pagennum)
        return render(req,"blog/index.html",locals())
@cache_page(60*5)
def index(req):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    pagennum = req.GET.get("page")
    pagennum = 1 if pagennum == None else pagennum
    page = paginator.get_page(pagennum)
    return render(req, "blog/index.html", locals())


class SingleView(View):
    def get(self,req,id):
        article = get_object_or_404(Article,pk=id)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        article.body = md.convert(article.body)
        article.toc = md.toc




        cf = CommentForm()
        return render(req, "blog/single.html",locals())
    def post(self,req,id):
        # cf =CommentForm(req.POST)
        # if cf.is_valid():
        #     cf.save(commit=False)
        #     article = get_object_or_404(Article,pk=id)
        #     cf.article = article
        #     cf.save()
        #     return HttpResponse("评论成功")
        name = req.POST.get("name")
        url = req.POST.get("url")
        eamil = req.POST.get("email")
        content = req.POST.get("content")

        comment = Comment()
        comment.name = name
        comment.url = url
        comment.email = eamil
        comment.content = content
        comment.article = get_object_or_404(Article,pk=id)

        comment.save()
        return redirect(reverse("blog:single",args=(id,)))

class ArchivesView(View):
    def get(self,req,year,month):
        articles = Article.objects.filter(create_time__year=year,create_time__month=month)
        paginator = Paginator(articles,2)
        pagenum = req.GET.get("page")
        page = paginator.get_page(pagenum)
        pagenum =1 if pagenum==None else pagenum
        page.path = "/archives/%s/%s" % (year, month)
        return render(req, "blog/index.html", locals())

class CategoryView(View):
    def get(self,req,id):
        category = get_object_or_404(Category,pk=id)
        articles = category.article_set.all()
        paginator = Paginator(articles, 2)
        pagenum = req.GET.get("page")
        page = paginator.get_page(pagenum)
        pagenum = 1 if pagenum == None else pagenum
        page.path = "/category/%s" % (id,)
        return render(req, "blog/index.html", locals())

class TagView(View):
    def get(self,req,id):
        tag = get_object_or_404(Tag,pk=id)
        articles = tag.article_set.all()
        paginator = Paginator(articles, 2)
        pagenum = req.GET.get("page")
        page = paginator.get_page(pagenum)
        pagenum = 1 if pagenum == None else pagenum
        page.path = "/tags/%s" % (id,)
        return render(req, "blog/index.html", locals())

class ContactView(View):
    def get(self,req):
        return render(req,"blog/contact.html")