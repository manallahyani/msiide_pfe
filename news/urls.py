from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail'),
    url(r'^panel/news/list/$', views.news_list, name='news_list'),
    url(r'^panel/news/add/$', views.add_news,name='add_news'),
    url(r'^panel/news/del/(?P<pk>\d+)/$', views.delete_news,name='delete_news'),
    url(r'^panel/news/edit/(?P<pk>\d+)/$', views.edit_news,name='edit_news'),
    
    
    

    
]