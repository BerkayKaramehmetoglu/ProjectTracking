from django.shortcuts import render


def pages(request):
    return render(request, 'pagesTemplate/pages.html')


def myproject(request):
    return render(request, 'pagesTemplate/myproject.html')


def projects(request):
    return render(request, 'pagesTemplate/projects.html')


def register(request):
    return render(request, 'pagesTemplate/register.html')


def projectname(request, project_name):
    data = {
        'project_name': project_name
    }
    return render(request, 'pagesTemplate/myproject.html', data)
# Create your views here.
