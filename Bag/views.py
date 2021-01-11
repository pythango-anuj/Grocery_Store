from django.shortcuts import render,redirect
from .models import Bag
from Bag.models import custom_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request,*args,**kwargs):
    items=Bag.objects.all().filter(username=request.user)
    args={'items':items}
    return render(request,'HTML/index.html',args)

@login_required
def add(request,*args,**kwargs):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_quantity = request.POST.get('item_quantity')
        item_status = request.POST.get('item_status')
        date = request.POST.get('date')
        item = Bag()
        item.username = request.user
        item.item_name = item_name
        item.item_quantity = item_quantity
        item.item_status = item_status
        item.date = date
        item.save()
        return redirect('Index')
    return render(request,'HTML/add.html')

@login_required
def edit(request,pk,*args,**kwargs):
    item = Bag.objects.get(pk=pk)
    args={'item':item}
    return render(request,'HTML/update.html',args)

@login_required
def update(request,pk,*args,**kwargs):
    item=Bag.objects.get(pk=pk)
    item.item_name = request.POST.get('item_name')
    item.item_quantity = request.POST.get('item_quantity')
    item.item_status = request.POST.get('item_status')
    item.date = request.POST.get('date')
    item.save()
    return redirect('Index')

@login_required
def delete_item(request,pk,*args,**kwargs):
    item=Bag.objects.all().filter(pk=pk)
    if item is not None:
        item.delete()
        return redirect('Index')
    return render(request,'HTML/index.html')

@login_required
def filter(request,*args,**kwargs):
    date = request.POST.get('date')
    items = Bag.objects.all().filter(username=request.user).filter(date=date)
    args = {'items':items}
    return render(request,'HTML/index.html',args)

