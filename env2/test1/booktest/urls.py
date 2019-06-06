from django.conf.urls import url
from .views import index,list,detail
app_name = "booktest"
urlpatterns=[
    url(r'^$',index,name='index'),
    url(r'^cjc/list/$',list,name='list'),
    url(r'^ggz/detail/(\d+)/$',detail,name='detail')
]