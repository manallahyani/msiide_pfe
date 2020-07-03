from django.shortcuts import render, get_object_or_404, redirect
from .models import Trending
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
import datetime


def add_trending(request):
     #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
    if request.method=='POST':
        txt=request.POST.get('txt')
        if txt=="":
            error='All Field REQUIED'
            return render(request,'back/error.html',{'error':error})
        
        b=Trending(txt=txt.capitalize())
        b.save()
    trendinglist=Trending.objects.all()

        
    return render(request,'back/trending.html',{'trendinglist':trendinglist})

def delete_trending(request,pk):
      #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
    try:
        b=Trending.objects.get(pk=pk)
        b.delete()
    except:
        error='Something is wrong'
        return render(request,'back/error.html',{'error':error})
    return redirect('add_trending')


def edit_trending(request,pk):
     #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
    if len(Trending.objects.filter(pk=pk))==0:
        error='Trending Not Found'
        return render(request,'back/error.html',{'error':error})

    
    trend=Trending.objects.get(pk=pk).txt
    
    if request.method=='POST':
        txt=request.POST.get('txt')
        if txt == '':
            error='ALL FIELD REQUIED'
            return render(request,'back/error.html',{'error':error})
           
        b=Trending.objects.get(pk=pk)
        b.txt=txt.capitalize() 
        b.save()
        return redirect('add_trending')

    return render(request,'back/edit_trending.html',{'pk':pk ,'trend':trend})