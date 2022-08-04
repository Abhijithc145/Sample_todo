from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.


def mytodo(request):
    task = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'index.html',{'task':task,'form':form})


def deleteItem(request,pk):
    task = Todo.objects.get(id=pk)
    task.delete()
    return redirect('/')


def updateItem(request,pk):
    todo = Todo.objects.get(id=pk)
    updateform = TodoForm(instance=todo)
    if request.method == 'POST':
        updateform = TodoForm(request.POST,instance = todo)
        if updateform.is_valid():
            updateform.save()
            return redirect('/')
    return render(request,'Update.html',{"todo":todo,"updateform":updateform})