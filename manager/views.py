from django.shortcuts import render, get_object_or_404, redirect
from .models import Manager
from news.models import News
from cat.models import Cat
from trending.models import Trending
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.core.files.storage import FileSystemStorage
import random
from random import randint
from django.contrib.contenttypes.models import ContentType
# Create your views here.

def manager_list(request):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    manager = Manager.objects.all()
    return render(request,'back/manager_list.html',{'manager':manager})

def delete_manager(request,pk):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    manager = Manager.objects.get(pk=pk)
    b=User.objects.filter(username=manager.utxt)
    b.delete()
    manager.delete()
    return redirect(manager_list)

def manager_group(request):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
  
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    group = Group.objects.all().exclude(name="masteruser")

    return render(request, 'back/manager_group.html', {'group':group})

def add_group(request):
    
     #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
        #login check end
    
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    if request.method=='POST':
        name=request.POST.get('name')
        
        if len(Group.objects.filter(name=name)) != 0:
            error = 'This Group is Already Exist'
            return render(request,'back/error.html',{'error':error})
        
        b=Group(name=name.capitalize())
        b.save()

    return redirect('manager_group')


def delete_group(request,name):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    b=Group.objects.filter(name=name)
    b.delete()
    
    return redirect(manager_group)

def user_group(request,pk):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    manager = Manager.objects.get(pk=pk)
    #user = User.objects.get(username=manager.name)
    user = User.objects.get(username=manager.utxt)

    ugroup=[]
    for i in user.groups.all():
        ugroup.append(i.name)
    group = Group.objects.all().exclude(name='masteruser')
    u=manager.utxt

    return render(request,'back/user_group.html',{'ugroup':ugroup,'group':group,'pk':pk, 'u':u})


def add_usertogroup(request,pk):
    
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    if request.method == 'POST' :

        gname = request.POST.get('gname')

        #group = Group.objects.get(name=gname)
        g = Group.objects.get(name=gname)
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.utxt)
        user.groups.add(g)
    
    

    return redirect('user_group' , pk=pk)

def del_usertogroup(request,pk,name):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    group = Group.objects.get(name=name)
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)
    user.groups.remove(group)
    
    return redirect('user_group' , pk=pk)
def manager_perms(request):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
  
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    perms = Permission.objects.all()

    return render(request, 'back/manager_perms.html', {'perms':perms})
def delete_perms(request,name):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    b=Permission.objects.filter(name=name)
    b.delete() 
    return redirect(manager_perms)

def manager_perms_add(request):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
        
    if request.method == 'POST':

        name = request.POST.get('name')
        cname = request.POST.get('cname')

        if len(Permission.objects.filter(codename=cname)) == 0 :

            content_type = ContentType.objects.get(app_label='main', model='main')
            permission = Permission.objects.create(codename=cname, name=name, content_type=content_type)

        else:
            error = "This Codename Used Before"
            return render(request, 'back/error.html' , {'error':error})

    return redirect('manager_perms')
def user_perms(request,pk):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    manager = Manager.objects.get(pk=pk)
    #user = User.objects.get(username=manager.name)
    user = User.objects.get(username=manager.utxt)
    permission = Permission.objects.filter(user=user)
    u=manager.utxt

    uperms=[]
    for i in permission:
        uperms.append(i.name)
    perms = Permission.objects.all()
  

    return render(request,'back/user_perms.html',{'uperms':uperms,'perms':perms,'pk':pk, 'u':u})

def add_usertoperms(request,pk):
    
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    if request.method == 'POST' :

        pname = request.POST.get('pname')

        #group = Group.objects.get(name=gname)
        p = Permission.objects.get(name=pname)
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.utxt)
        

        user.user_permissions.add(p)
    
    

    return redirect('user_perms' , pk=pk)
def del_usertoperms(request,pk,name):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    perms = Permission.objects.get(name=name)
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)
    user.user_permissions.remove(perms)
    
    return redirect('user_perms' , pk=pk)

def group_perms(request,name):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    group = Group.objects.get(name=name)
    perms = group.permissions.all()

    allperms = Permission.objects.all()

    return render(request, 'back/group_perms.html',{'perms':perms,'allperms':allperms,'name':name,'group':group})

def group_perms_del(request,gname,name):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    group = Group.objects.get(name=gname)
    perm = Permission.objects.get(name=name)
    group.permissions.remove(perm)
 

    return redirect( 'group_perms', name=gname)

def group_perms_add(request,name):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    if request.method == 'POST':
        pname = request.POST.get('pname')
        group = Group.objects.get(name=name)
        perms = Permission.objects.get(name=pname)
        group.permissions.add(perms)
   
    return redirect( 'group_perms', name=name)
