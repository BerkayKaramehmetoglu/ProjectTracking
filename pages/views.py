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
    active_projects = ProjectModels.objects.filter(is_active=1)
    return render(request, 'pagesTemplate/projects.html', {
        'active_projects': active_projects
    })


def register(request):
    return render(request, 'pagesTemplate/register.html')
# Create your views here.
