from django.shortcuts import render

from .models import ProjectModels


def pages(request):
    return render(request, 'pagesTemplate/pages.html')


def myprojects(request):
    projects = ProjectModels.objects.all()
    return render(request, 'pagesTemplate/myproject.html', {
        'my_projects': projects
    })


def projects(request):
    projects = ProjectModels.objects.all()
    return render(request, 'pagesTemplate/projects.html', {
        'projects': projects
    })


def register(request):
    return render(request, 'pagesTemplate/register.html')
# Create your views here.
