from django.shortcuts import render
from django.http import HttpResponse

from todo_project.tasks.models import Task


def index(request):
    return render(request, 'tasks/task_list.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_delete(request, id):
    del_task = Task.objects.get(id=id).delete()
    return HttpResponse("Task Deleted")

def task_detail(request, id):
    task = Task.objects.get(id=id)