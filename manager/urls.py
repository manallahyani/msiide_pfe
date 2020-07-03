from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^panel/manager/list/$', views.manager_list, name='manager_list'),
    url(r'^panel/manager/del/(?P<pk>\d+)/$', views.delete_manager, name='delete_manager'),
    url(r'^panel/manager/group/$', views.manager_group, name='manager_group'),
    url(r'^panel/manager/group/add/$', views.add_group, name='add_group'),
    url(r'^panel/manager/group/del/(?P<name>.*)/$', views.delete_group, name='delete_group'),
    url(r'^panel/user/group/(?P<pk>\d+)/$', views.user_group, name='user_group'),
    url(r'^panel/add/user/togroup/(?P<pk>\d+)/$', views.add_usertogroup, name='add_usertogroup'),
    url(r'^panel/del/user/togroup/(?P<pk>\d+)/(?P<name>.*)/$', views.del_usertogroup, name='del_usertogroup'),
    url(r'^panel/manager/permissions/$', views.manager_perms, name='manager_perms'),
    url(r'^panel/manager/permission/del/(?P<name>.*)/$', views.delete_perms, name='delete_perms'),
    url(r'^panel/manager/add/permessions/$', views.manager_perms_add, name='manager_perms_add'),
    url(r'^panel/user/permission/(?P<pk>\d+)/$', views.user_perms, name='user_perms'),
    url(r'^panel/add/user/topermissions/(?P<pk>\d+)/$', views.add_usertoperms, name='add_usertoperms'),
    url(r'^panel/del/user/topermission/(?P<pk>\d+)/(?P<name>.*)/$', views.del_usertoperms, name='del_usertoperms'),
    url(r'^panel/group/permission/(?P<name>.*)/$', views.group_perms, name='group_perms'),
    url(r'^panel/group/del/permission/(?P<gname>.*)/(?P<name>.*)/$', views.group_perms_del, name='group_perms_del'),
    url(r'^panel/group/add/permission/(?P<name>.*)/$', views.group_perms_add, name='group_perms_add'),

]