from Tools.scripts.make_ctype import method
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from task.forms import Todoform
from task.models import Task
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView
class TaskList(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'det'

class Taskdetail(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'det'

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'det'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url =  reverse_lazy('cbvhome')

def tasking(request):
        if request.method == 'POST':
            name = request.POST.get("name")
            priority = request.POST.get("priority")
            date = request.POST.get("date")
            print(name)
            print(priority)
            task = Task(name=name, priority=priority,date=date)
            task.save()
            det1 = Task.objects.all()
            return render(request, 'home.html', {'det': det1})
        det1 = Task.objects.all()
        return render(request, 'home.html', {'det': det1})


def detail(request):
    det1 = Task.objects.all()
    return render(request, 'detail.html', )


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect("/")
    return render(request, 'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=Todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')

    return render(request,'edit.html',{'f':f,'task':task})

