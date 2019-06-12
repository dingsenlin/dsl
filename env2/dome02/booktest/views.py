from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import VoteInfo1,VoteInfo2
from django.views.generic import View
from .forms import LoginForm

# Create your views here.
#装饰器
def checklogin(fun):
    def check(req,*args):
        # if req.COOKIES.get("username"):
        #     return fun(req,*args)
        if req.session.get('username'):
            return fun(req,*args)
        else:
            return redirect(reverse("booktest:login"))
    return check

@checklogin
def index(req):
    # return HttpResponse("index")
    return render(req, 'booktest/index.html',locals())

@checklogin
def detail(req,id):
    vote = VoteInfo1.objects.get(pk=id)
    # return HttpResponse("detail %s"% id)
    if req.method == "GET":
        return render(req, 'booktest/detail.html', locals())
    elif req.method == "POST":

        res = VoteInfo2.objects.get(name=req.POST.get('ppt'))
        res.option += 1
        res.save()
        vote2 = vote.voteinfo2_set.all()
        return render(req, 'booktest/result.html', locals())

@checklogin
def list(req):
    vote1 = VoteInfo1.objects.all()
    return render(req, 'booktest/list.html', locals())
    # return HttpResponse("list")


@checklogin
def result(req, id):
    return render(req, 'booktest/result.html',locals())


def login(req):

    if req.method == "GET":
        # lf = LoginForm()
        #
        # return render(req,"booktest/login.html",locals())
        pass

    elif req.method == "POST":
        # username = req.POST.get("username")
        # pwd = req.POST.get("password")
        # # print(username,pwd)
        # # cookie实在response里设置
        # # res = redirect(reverse("booktest:index"))
        # # res.set_cookie("username",username)
        # # return res
        # #session  在request里面设置
        # req.session["username"] = username
        # lf = LoginForm(req.POST)
        # print(lf.is_valid())
        # return redirect(reverse("booktest:index"))
        pass
def regist(req):
    if req.method == "GET":
        return render(req, "booktest/regist.html")
    elif req.method == "POST":
        username = req.POST.get("username")
        pwd = req.POST.get("password")
        req.session["username"] = username
        return redirect(reverse("booktest:index"))