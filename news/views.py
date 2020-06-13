from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
import datetime
from django.core.files.storage import FileSystemStorage





# Create your views here.
def news_detail(request, word):
    site = Main.objects.get(pk=1)
    news = News.objects.filter(name=word)
    
    return render(request,'front/news_detail.html',{'news':news , 'site':site})


def news_list(request):
    news=News.objects.all()
    return render(request,'back/news_list.html',{'news':news})

def add_news(request):
    date=datetime.datetime.now()
    year=str(date.year)
    month=str(date.month)
    day=str(date.day)
    hour=str(date.hour)
    minute=str(date.minute)
    second=str(date.second)
    date=day+'-'+month+'-'+year+' '+hour+':'+minute+':'+second
    if request.method=='POST':
        newstitle=request.POST.get('newstitle')
        newscat=request.POST.get('newscat')
        newsdesc=request.POST.get('newsdesc')
        newstxt=request.POST.get('newstxt')

        if newstitle=='' or newscat=='' or newsdesc=='' or newstxt=='':
            error='ALL FIELD REQUIED'
            return render(request,'back/error.html',{'error':error})
        try:
            myfile= request.FILES['myfile']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name, myfile)
            url= fs.url(filename)
            if str(myfile.content_type).startswith('image'):
                if myfile.size<5000000:
                    b=News(name=newstitle.title(), catname=newscat, desc=newsdesc, txt_body=newstxt, date=date, picurl=url, picname=filename, writer='-', views=0, catid=0)
                    b.save()
                    return redirect('news_list')
                else:
                    error='Your File is Bigger Than 5 Mb'
                    return render(request,'back/error.html',{'error':error})

            else:
                fs=FileSystemStorage()
                fs.delete(filename)
                error='Your File Not Supported'
                return render(request,'back/error.html',{'error':error})

        except:
            error='Please Input Your File'
            return render(request,'back/error.html',{'error':error})
    return render(request,'back/add_news.html')
def delete_news(request,pk):
    try:
        b=News.objects.get(pk=pk)
        fs=FileSystemStorage()
        fs.delete(b.picname)
        b.delete()
    except:
        error='Something is wrong'
        return render(request,'back/error.html',{'error':error})
    return redirect(news_list)
