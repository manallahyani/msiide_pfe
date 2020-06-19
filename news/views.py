from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
import datetime
from django.core.files.storage import FileSystemStorage
from subcat.models import SubCat
from cat.models import Cat





# Create your views here.
def news_detail(request, word):
    site = Main.objects.get(pk=1)
    site = Main.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat=Cat.objects.all()
    subcat= SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-show')
    shownews = News.objects.filter(name=word)
  
    mynews=News.objects.get(name=word)
    mynews.show=mynews.show + 1
    mynews.save()
  
    return render(request,'front/news_detail.html',{'news':news , 'site':site,'cat':cat,'subcat':subcat, 'lastnews':lastnews,'shownews':shownews})


def news_list(request):
    #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
    
    news=News.objects.all()
    return render(request,'back/news_list.html',{'news':news})

def add_news(request):
     #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
    cat = SubCat.objects.all()
    date=datetime.datetime.now()
    year=date.year
    month=date.month
    day=date.day
    if len(str(day))== 1:
        day = '0'+str(day)
    
    if len(str(month))== 1:
        month='0'+str(month)
    today=str(day)+"/"+str(month)+"/"+str(year)
    
    hour = date.hour
    minute = date.minute
    if len(str(hour))== 1:
        hour = '0'+str(hour)
    
    if len(str(minute))== 1:
        minute='0'+str(minute)
    time = str(hour)+":"+str(minute)
    print('time is ',today,time)

    time = str(date.hour)+":"+str(date.minute)+":"+str(date.second)
    if request.method=='POST':
        newstitle=request.POST.get('newstitle')
        newscat=request.POST.get('newscat')
        newsdesc=request.POST.get('newsdesc')
        newstxt=request.POST.get('newstxt')
        newsid=request.POST.get('newscat')

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
                    newsname = SubCat.objects.get(pk=newsid).name
                    ocatid = SubCat.objects.get(pk=newsid).catid
                    b=News(name=newstitle.title(), catname=newsname,catid=newsid, desc=newsdesc, txt_body=newstxt, date=today,time=time, picurl=url,ocatid=ocatid, picname=filename, writer='-', show=0)
                    b.save()
                    count=len(News.objects.filter(ocatid=ocatid))
                    b=Cat.objects.get(pk=ocatid)
                    b.count=count
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
            error='Please Input Your Image'
            return render(request,'back/error.html',{'error':error})
    return render(request,'back/add_news.html',{'cat':cat})
    
def delete_news(request,pk):
    try:
        b = News.objects.get(pk=pk)

        fs = FileSystemStorage()
        fs.delete(b.picname)

        ocatid = News.objects.get(pk=pk).ocatid

        b.delete()

        
        count = len(News.objects.filter(ocatid=ocatid))

        m = Cat.objects.get(pk=ocatid)
        m.count = count
        m.save()
        
    except:
        error='Something is wrong'
        return render(request,'back/error.html',{'error':error})
    return redirect(news_list)

def edit_news(request,pk):
     #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
    if len(News.objects.filter(pk=pk))==0:
        error='News Not Found'
        return render(request,'back/error.html',{'error':error})

    
    news=News.objects.get(pk=pk)
    cat=SubCat.objects.all()
    if request.method=='POST':
        newstitle=request.POST.get('newstitle')
        newscat=request.POST.get('newscat')
        newsdesc=request.POST.get('newsdesc')
        newstxt=request.POST.get('newstxt')
        newsid=request.POST.get('newscat')

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
                    newsname = SubCat.objects.get(pk=newsid).name
                    b=News.objects.get(pk=pk)

                    fss=FileSystemStorage()
                    fss.delete(b.picname)

                    b.name=newstitle
                    b.newsdesc=newsdesc
                    b.newstxt=newstxt
                    b.picname=filename
                    b.picurl=url
                    b.writer="-"
                    b.catname=newsname
                    b.catid=newsid
                    b.save()
                    return redirect('news_list')
                
                else:
                    fs=FileSystemStorage()
                    fs.delete(filename)
                    error='Your File is Bigger Than 5 Mb'
                    return render(request,'back/error.html',{'error':error})
            else:
                fs=FileSystemStorage()
                fs.delete(filename)
                error='Your File Not Supported'
                return render(request,'back/error.html',{'error':error})
            

        except:
            
            newsname = SubCat.objects.get(pk=newsid).name


            b=News.objects.get(pk=pk)
            b.name=newstitle
            b.newsdesc=newsdesc
            b.newstxt=newstxt
            b.catname=newsname
            b.catid=newsid
        
            b.save()
            error='Your File Not Supported'
            return redirect('news_list')

    return render(request,'back/edit_news.html',{'pk':pk ,'news':news, 'cat':cat})

