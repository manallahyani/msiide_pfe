from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
import datetime





# Create your views here.
def news_detail(request, word):
    site = Main.objects.get(pk=1)
    news = News.objects.filter(name=word)
    
    return render(request,'front/news_detail.html',{'news':news , 'site':site})


def news_list(request):
    news=News.objects.all()
    return render(request,'back/news_list.html',{'news':news})

def add_news(request):
    if request.method=='POST':
        newstitle=request.POST.get('newstitle')
        newscat=request.POST.get('newscat')
        newsdesc=request.POST.get('newsdesc')
        newstxt=request.POST.get('newstxt')

        if newstitle=='' or newscat=='' or newsdesc=='' or newstxt=='':
            error='ALL FIELD REQUIED'
            return render(request,'back/error.html',{'error':error})
        b=News(name=newstitle, catname=newscat, desc=newsdesc, txt_body=newstxt, date=datetime.date, pic="-", writer='-', views=0, catid=0)
        b.save()
        return redirect('news_list')
    return render(request,'back/add_news.html')

