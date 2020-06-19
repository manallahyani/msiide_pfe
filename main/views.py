from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home(request):
    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat=Cat.objects.all()
    subcat= SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-show')
    

    #site = 'MySite| Home'
    return render(request,'front/home.html',{'site':site ,'news':news,'cat':cat,'subcat':subcat, 'lastnews':lastnews, 'popnews':popnews})


def about(request):
    site = Main.objects.get(pk=1)
    return render(request,'front/about.html',{'site':site})

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
    

