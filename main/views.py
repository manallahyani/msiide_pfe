from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
from cat.models import Cat
from trending.models import Trending
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import random
from random import randint
from manager.models import Manager



# Create your views here.
def home(request):
    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    latest = News.objects.all().order_by('-pk')[:6]
    
    cat=Cat.objects.all()
    subcat= SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]
    trend=Trending.objects.all().order_by('-pk')

    #random_object=Trending.objects.all()[randint (0,len(trend) -1)] 
    #to not show the same trending after every refresh to the web site 
    #print(random_object)
    

    #site = 'MySite| Home'
    return render(request,'front/home.html',{'site':site ,'news':news,'cat':cat,'subcat':subcat, 'lastnews':lastnews, 'popnews':popnews,'popnews2':popnews2,'trend':trend,'latest':latest})


def about(request):
    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat=Cat.objects.all()
    subcat= SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-show')[:4]
    popnews2 = News.objects.all().order_by('-show')[:3]
    trend=Trending.objects.all().order_by('-pk')
    
    return render(request,'front/about.html',{'site':site,'cat':cat,'subcat':subcat, 'news':news, 'lastnews':lastnews, 'popnews':popnews,'popnews2':popnews2,'trend':trend})

def panel(request):
    #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
    return render(request,'back/home.html')
def mylogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username != '' and password !='':
            user=authenticate(username=username,password=password)
            if user != None:
                login(request,user)
                return redirect('panel')
        
    return render(request,'front/login.html')

def mylogout(request):
    logout(request)
    return redirect('mylogin')

def site_setting(request):
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
    
    if request.method == 'POST' :
        name= request.POST.get('name')
        tel= request.POST.get('tel')
        fb= request.POST.get('fb')
        tw= request.POST.get('tw')
        yt= request.POST.get('yt')
        link= request.POST.get('link')
        about= request.POST.get('about')

        if fb == "": fb = "#"
        if tw == "": tw = "#"
        if yt == "": yt = "#"
        if link == "": link = "#"

        if name == "" or tel == "" or about == "":
            error='ALL FIELD REQUIED'
            return render(request,'back/error.html',{'error':error})
            
        try:
            myfile= request.FILES['myfile']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name, myfile)
            url= fs.url(filename)
            picurl=url
            picname=filename
        except:
            picurl="-"
            picname="-"
        
        try:
            myfile2= request.FILES['myfile2']
            fss=FileSystemStorage()
            filename2=fss.save(myfile2.name, myfile2)
            url2= fss.url(filename2)
            picurl2=url2
            picname2=filename2
        except:
            picurl2="-"
            picname2="-"
        



        b=Main.objects.get(pk=1)
        b.name = name
        b.tel=tel
        b.fb=fb
        b.tw=tw
        b.yt=yt
        b.link=link
        b.about=about
        if picurl != "-": b.picurl=picurl
        if picname != "-": b.picname=picname
        if picurl2 != "-": b.picurl2=picurl2
        if picname2 != "-": b.picname2=picname2
        b.save()
    
    site=Main.objects.get(pk=1)
    return render(request,'back/setting.html',{'site':site})        
    

def about_setting(request):
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
    about=Main.objects.get(pk=1)
    if request.method == 'POST':
        txt= request.POST.get('txt')

        if txt == "":
            error='ALL FIELD REQUIED'
            return render(request,'back/error.html',{'error':error})
        
        b=Main.objects.get(pk=1)
        b.abouttxt=txt
        b.save()
    about=Main.objects.get(pk=1).abouttxt
    return render(request,'back/about_setting.html',{'about':about}) 

def contact(request):
    
    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat=Cat.objects.all()
    subcat= SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-show')[:4]
    popnews2 = News.objects.all().order_by('-show')[:3]
    trend=Trending.objects.all().order_by('-pk')
    return render(request,'front/contact.html',{'site':site,'cat':cat,'subcat':subcat, 'news':news, 'lastnews':lastnews, 'popnews':popnews,'popnews2':popnews2,'trend':trend}) 


def change_pass(request):
     #login check start
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

        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')

        if oldpass == "" or newpass == "" :
            error = "All Fields Requirded"
            return render(request, 'back/error.html' , {'error':error})

        user = authenticate(username=request.user, password=oldpass)

        if user != None :

            if len(newpass) < 8 :
                error = "Your Password Most Be At Less 8 Character"
                return render(request, 'back/error.html' , {'error':error})

            
            count1 = 0
            count2 = 0
            count3 = 0 
            count4 = 0

            for i in newpass :

                if i > "0" and i < "9" :
                    count1 = 1
                if i > "A" and i < "Z" :
                    count2 = 1
                if i > 'a' and i < 'z' :
                    count3 = 1
                if i > "!" and i < "(" :
                    count4 = 1

            if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 :
                user = User.objects.get(username=request.user)
                user.set_password(newpass)
                user.save()
                return redirect('mylogout')

            else:

                error = "Your Password Is Not Correct"
                return render(request, 'back/error.html' , {'error':error})


    return render(request, 'back/change_pass.html')


def myregister(request):
    
    if request.method == 'POST':
        name= request.POST.get('name')
        uname= request.POST.get('uname')
        uemail= request.POST.get('uemail')
        upassword= request.POST.get('upassword')
        upassword_v= request.POST.get('upassword_v')

        if upassword != upassword_v:
            msg="Your password didn't match"
            return render(request,'front/msgbox.html',{'msg':msg})
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for i in upassword:
            if i > "0" and i < "9":
                count1 = 1
            if i > "a" and i < "z":
                count2 = 1
            if i > "A" and i < "Z":
                count3 = 1
            if i > "!" and i < "(":
                count4 = 1
        if count1 == 0 or count2 == 0 or count3 == 0:
            msg="Your password is not strong"
            return render(request,'front/msgbox.html',{'msg':msg})
        if len(upassword)<8:
            msg="Your password should contient more than 8 characters"
            return render(request,'front/msgbox.html',{'msg':msg})
            print(count1,count2,count3,count4)
        if len(User.objects.filter(username=uname))==0 and len(User.objects.filter(email= uemail))==0 :
            user = User.objects.create_user(username=uname,email=uemail,password=upassword)
            
            b = Manager(name=name,utxt=uname,email=uemail)
            b.save()
            
            msg="register Succesful"
            return render(request,'front/msgbox.html',{'msg':msg})

        else:
            msg="This user already exist"
            return render(request,'front/msgbox.html',{'msg':msg})
            



            
            
    return render(request,'front/login.html')