from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contact/msgbox/$', views.contact_add,name='contact_add'),
    url(r'^panel/contact/list/$', views.contact_list,name='contact_list'),
    url(r'^panel/msg/del/(?P<pk>\d+)/$', views.delete_msg,name='delete_msg'),

    

]