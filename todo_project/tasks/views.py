from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'tasks/task_list.html')

def task_list(request):
    return list([1,2,3])
