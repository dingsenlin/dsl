from django.shortcuts import render
from django.http import HttpResponse
from .models import VoteInfo1,VoteInfo2
# Create your views here.

def index(req):
    # return HttpResponse("index")
    return render(req, 'booktest/index.html',{ "username":"dsl" })

def detail(req,id):
    vote = VoteInfo1.objects.get(pk=id)
    # return HttpResponse("detail %s"% id)
    if req.method == "GET":
        return render(req, 'booktest/detail.html', {"vote": vote})
    elif req.method == "POST":

        res = VoteInfo2.objects.get(name=req.POST.get('ppt'))
        res.option += 1
        res.save()
        vote2 = vote.voteinfo2_set.all()
        return render(req, 'booktest/result.html', {'vote': vote, 'vote2': vote2})

def list(req):
    vote1 = VoteInfo1.objects.all()
    return render(req, 'booktest/list.html', {"vote1": vote1})
    # return HttpResponse("list")


def result(req, id):
    return render(req, 'booktest/result.html', {})
