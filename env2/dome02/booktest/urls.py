from django.conf.urls import url
from .views import index,list,detail,result,login
app_name = "booktest"
urlpatterns=[
    url(r'^$',index,name='index'),
    url(r'^list/$',list,name='list'),
    url(r'^detail/(\d+)/$',detail,name='detail'),
    url(r'^result/(\d+)/$',result,name='result'),
    url(r'^login/$',login, name="login"),
]

