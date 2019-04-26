from django.conf.urls import url
from . import views

# 第一个参数：网址
# 第二各参数：处理的函数
# 第三个参数：处理函数的别名
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]

'''
被括起来的部分 (?P<pk>[0-9]+) 匹配 255，
那么这个 255 会在调用视图函数 detail 时被传递进去，
实际上视图函数的调用就是这个样子：detail(request, pk=255)
(?P<name>…)
（命名组合）类似正则组合，但是匹配到的子串组在外部是通过定义的 name 来获取的。
'''