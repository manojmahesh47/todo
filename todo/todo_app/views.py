from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import todo_form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class Deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todo_app:hom')
class TaskKistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'
class Detailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
class Updateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields=['name','priority','date']
    def get_success_url(self):
        return reverse_lazy('todo_app:details',kwargs={'pk':self.object.id})
def add(request):
    task1 = Task.objects.all()

    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')

        # Corrected the date assignment
        task = Task(name=name, priority=priority, date=date)
        task.save()

    return render(request, 'home.html', {'task': task1})
def update(request, taskid):
    task = Task.objects.get(id=taskid)
    fm = todo_form(request.POST or None, instance=task)

    if request.method == 'POST':
        if fm.is_valid():
            fm.save()
            return redirect('/')

    return render(request, 'update.html', {'fm': fm, 'task': task})
def details(request):
    task=Task.objects.all()
    return render(request,'details.html',{'task':task})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')

    return render(request,'delete.html')

