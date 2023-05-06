from django.shortcuts import render, redirect

from .models import ProjectModels


def pages(request):
    return render(request, 'pagesTemplate/pages.html')


def myprojects(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        project_description = request.POST['project_description']
        project_technology = request.POST['project_technology']
        is_active = request.POST.get('is_active', False)
        if is_active == 'on':
            is_active = True
        project = ProjectModels(project_name=project_name, project_description=project_description,
                                project_technology=project_technology, is_active=is_active)
        project.save()
        return redirect('/myproject')
    my_projects = ProjectModels.objects.all()
    return render(request, 'pagesTemplate/myproject.html', {
        'my_projects': my_projects, })


def projects(request):
    projects = ProjectModels.objects.all()
    return render(request, 'pagesTemplate/projects.html', {
        'projects': projects,
    })


def register(request):
    return render(request, 'pagesTemplate/register.html')
# Create your views here.
