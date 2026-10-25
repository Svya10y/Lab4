from django.shortcuts import render
from django.http import Http404
from .models import Task


def archive(request):
    return render(request, 'archive.html', {"posts": Task.objects.all()})


def get_task(request, task_id):
    try:
        post = Task.objects.get(id=task_id)
        return render(request, 'task.html', {"post": post})
    except Task.DoesNotExist:
        raise Http404
