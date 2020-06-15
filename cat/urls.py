from django.conf.urls import url
from . import views

urlpatterns = [
  
    url(r'^panel/category/list/$', views.cat_list, name='cat_list'),
    url(r'^panel/category/add/$', views.add_cat, name='add_cat'),
    url(r'^panel/category/del/(?P<pk>\d+)/$', views.delete_cat,name='delete_cat'),
    

]