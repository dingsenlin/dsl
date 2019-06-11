from django.conf.urls import url
from .views import index,list,detail,result
urlpatterns=[
    url(r'^$',index,name='index'),
    url(r'^list/$',list,name='list'),
    url(r'^detail/(\d+)/$',detail,name='detail'),
    url(r'^result/(\d+)/$',result,name='result')
]

