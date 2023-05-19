from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MyProjectForm, MyProjectUpdateForm
from .models import ProjectModels


@login_required()
def myprojects(request):
    projects = ProjectModels.objects.filter(project_owner=request.user)
    if request.method == 'POST':
        form = MyProjectForm(request.POST)

        if form.is_valid():
            form.instance.project_owner = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 f'Your Project Has been Created {form.cleaned_data["project_name"]}')
            return redirect('/myproject/')
    else:
        form = MyProjectForm()
        return render(request, 'pagesTemplate/myproject.html', {
            'form': form,
            'projects': projects})


@login_required()
def projects(request):
    projects = ProjectModels.objects.all()
    return render(request, 'pagesTemplate/projects.html', {
        'projects': projects,
    })


def update(request, id):
    projects = get_object_or_404(ProjectModels, pk=id)
    if request.method == 'POST':
        form = MyProjectUpdateForm(request.POST, instance=projects)
        form.save()
        messages.add_message(request, messages.SUCCESS,
                             f'Update Successful {projects.project_name}')
        return redirect('/myproject/')
    else:
        form = MyProjectUpdateForm(instance=projects)
    return render(request, 'pagesTemplate/update_projects.html', {'form': form})


def delete(request, id):
    projects = get_object_or_404(ProjectModels, pk=id)
    if request.method == 'POST':
        projects.delete()
        messages.add_message(request, messages.ERROR,
                             f'{projects.project_name} Your Project Has Been Delete')
        return redirect('/myproject/')
    return render(request, 'pagesTemplate/myproject.html', {'projects': projects})


def owner_list(request):
    projects = ProjectModels.objects.all()
    if request.method == 'POST':
        if 'add' in request.POST:
            project = projects.filter(id=request.POST.get('add')).first()
            project.add = True
            project.save()
            return render(request, 'pagesTemplate/project_owner_list.html', {'projects': projects})

        if 'dont_add' in request.POST:
            project = projects.filter(id=request.POST.get('dont_add')).first()
            project.add = False
            project.save()
            return render(request, 'pagesTemplate/project_owner_list.html', {'projects': projects})
    else:
        return render(request, 'pagesTemplate/project_owner_list.html', {
            'projects': projects,
        })


def authorized(request):
    users = User.objects.all()

    if request.method == 'POST':
        if 'authorized' in request.POST:
            user = users.filter(id=request.POST.get('authorized')).first()
            user.is_superuser = True
            user.is_staff = True
            user.save()
            return render(request, 'pagesTemplate/authorize.html', {'users': users})

        elif 'create_admin' in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            re_password = request.POST['re_password']

            if password == re_password:
                if User.objects.filter(username=username).exists():
                    return render(request, 'pagesTemplate/authorize.html')

                elif User.objects.filter(email=email).exists():
                    return render(request, 'pagesTemplate/authorize.html')

                else:
                    user = User.objects.create_superuser(username=username, email=email,
                                                         password=password)
                    user.save()
                    return redirect('/authorize/')
            else:
                return render(request, 'pagesTemplate/authorize.html')

    else:
        return render(request, 'pagesTemplate/authorize.html', {'users': users})

# Create your views here.
