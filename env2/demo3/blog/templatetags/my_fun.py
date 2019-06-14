from django.template import Library
from ..models import Article,Category,Tag
register = Library()

@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.all().order_by("-create_time")[:num]

@register.simple_tag
#dates 第一个字段是需要处理的字段(现为时间字段) 第二个字段是去重字段,显示上传需要去重的项目(现显示的是需要去重的年和月)
def getarchives():
    result = Article.objects.dates("create_time","month")
    return result

@register.simple_tag
def getcategorys():
    return Category.objects.all()

@register.simple_tag
def gettags():
    return Tag.objects.all()