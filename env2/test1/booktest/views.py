from django.shortcuts import render
from django.http import HttpResponse
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
