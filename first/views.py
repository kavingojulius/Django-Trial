from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Items
from .foms import AddItems
# Create your views here.

def index(request):
    items = Items.objects.all()
    context = {
        'items':items
    }
    return render(request, 'index.html',context)

def add(request):        
    if request.method == 'POST':
        form = AddItems(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddItems()

    context = {
        'form':form
    }
    return render(request, 'add.html', context)

def update(request,id):
    item = Items.objects.get(id=id)
    if request.method == 'POST':
        form = AddItems(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddItems(instance=item)
    context = {
        'form':form
    }

    return render(request, 'update.html',context)

def delete(request,id):

    try:
        item = Items.objects.get(id=id)
    except:
        return HttpResponse('Item not found')
    item.delete()
    return redirect('index')




