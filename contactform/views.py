from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactForm
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
import datetime


def contact_add(request):
   
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
        name=request.POST.get('name')
        email=request.POST.get('email')
        txt=request.POST.get('txt')
        

        if name=='' or email=='' or txt=='':
            msg='ALL FIELD REQUIED'
            return render(request,'front/msgbox.html',{'msg':msg})
        b=ContactForm(name=name.title(),email=email,txt=txt,date=today,time=time)
        b.save()
        msg='Your Message Received'
    return render(request,'front/msgbox.html',{'msg':msg})


def contact_list(request):
  #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
    contact=ContactForm.objects.all()
    return render(request,'back/contact_list.html',{'contact':contact})

def delete_msg(request,pk):
     #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
    try:
        b=ContactForm.objects.filter(pk=pk)
        b.delete()
    except:
        error='Something is wrong'
        return render(request,'back/error.html',{'error':error})
    return redirect(contact_list)

