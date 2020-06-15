from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat


def cat_list(request):
    cat=Cat.objects.all()
    return render(request,'back/cat_list.html',{'cat':cat})


def add_cat(request):
    if request.method=='POST':
        name=request.POST.get('name')
        if name=="":
            error='All Field REQUIED'
            return render(request,'back/error.html',{'error':error})
        if len(Cat.objects.filter(name=name)) != 0:
            error = 'This Category Already Exist'
            return render(request,'back/error.html',{'error':error})
        b=Cat(name=str(name).title())
        b.save()

        return redirect('cat_list')
    return render(request,'back/add_cat.html')

def delete_cat(request,pk):
    try:
        b=Cat.objects.get(pk=pk)
        b.delete()
    except:
        error='Something is wrong'
        return render(request,'back/error.html',{'error':error})
    return redirect(cat_list)

