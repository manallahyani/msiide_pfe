from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCat
from cat.models import Cat


def subcat_list(request):
     #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
    subcat=SubCat.objects.all()
    return render(request,'back/subcat_list.html',{'subcat':subcat})



def add_subcat(request):
     #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
    cat=Cat.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        catid=request.POST.get('cat')
        if name=="":
            error='All Field REQUIED'
            return render(request,'back/error.html',{'error':error})
        try:
            if len(SubCat.objects.filter(name=name)) != 0:
                error = 'This Category Already Exist'
                return render(request,'back/error.html',{'error':error})
            catname=Cat.objects.get(pk=catid).name
            b=SubCat(name=str(name).title(),catname=catname, catid=catid)
            b.save()
            return redirect('subcat_list')
        except:
            error="Something Is Wrong; Select a Category"
            return render(request,'back/error.html',{'error':error})
    return render(request,'back/add_subcat.html',{'cat':cat})

def delete_subcat(request,pk):
    try:
        b=SubCat.objects.get(pk=pk)
        b.delete()
    except:
        error='Something is wrong'
        return render(request,'back/error.html',{'error':error})
    return redirect(subcat_list)