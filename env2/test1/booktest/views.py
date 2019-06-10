from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import BookInfo,HeroInfo
# Create your views here.
def index(req):
    # temp = loader.get_template('booktest/index.html')
    # res = temp.render({ "username":"dsl" })
    # return HttpResponse(res)
    return render(req,'booktest/index.html',{ "username":"dsl" })

def list(req):
    books=BookInfo.objects.all()

    # temp = loader.get_template('booktest/list.html')
    # res = temp.render({"books":books})
    # return HttpResponse(res)
    return render(req,'booktest/list.html',{"books":books})

def detail(req,id):
    book=BookInfo.objects.get(pk=id)

    # temp = loader.get_template('booktest/detail.html')
    # res = temp.render({"book":book})
    # return HttpResponse(res)
    return render(req,'booktest/detail.html',{"book":book})

def deletehero(req,id):
    # return HttpResponse("删除%s",(id,))
    hero = HeroInfo.objects.get(pk=id)
    hero.delete()
    return HttpResponseRedirect("/detail/%s/"%(hero.book.id,))

def deletebook(req,id):
    # return HttpResponse("删除%s",(id,))
    book = BookInfo.objects.get(pk=id)
    book.delete()
    return HttpResponseRedirect("/list/")

def addhero(req,id):
    book = BookInfo.objects.get(pk=id)
    # return HttpResponse("添加成功%s"%(id,))
    if req.method == "GET":
        return render(req,"booktest/addhero.html", {"book":book})
    elif req.method == "POST":
        hero = HeroInfo()
        hero.name = req.POST.get("heroname")
        hero.content = req.POST.get("herocontent")
        hero.book = book
        hero.save()
        return HttpResponseRedirect("/detail/%s/"%(id,))

def addbook(req):
    # book = BookInfo.objects.get(pk=id)
    # return HttpResponse("添加成功")
    if req.method == "GET":
        return render(req,"booktest/addbook.html")
    elif req.method == "POST":
        book = BookInfo()
        book.title = req.POST.get("title")
        book.pub_date = req.POST.get("pub_date")
    #     hero.book = book
        book.save()
        # return redirect(reverse(" booktest:list "))
        return HttpResponseRedirect("/list/")