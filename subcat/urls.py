from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^panel/SubCategory/list/$', views.subcat_list, name='subcat_list'),
    url(r'^panel/SubCategory/add/$', views.add_subcat, name='add_subcat'),
    url(r'^panel/SubCategory/del/(?P<pk>\d+)/$', views.delete_subcat,name='delete_subcat'),
    
]