from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main





# Create your views here.
def news_detail(request, word):
    site = Main.objects.get(pk=1)
    news = News.objects.filter(name=word)
    
    return render(request,'front/news_detail.html',{'news':news , 'site':site})


def news_list(request):
    news=News.objects.all()
    return render(request,'back/news_list.html',{'news':news})

def add_news(request):
    
    return render(request,'back/add_news.html')

