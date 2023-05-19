from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def users(request):
    return render(request, 'usersTemplate/login.html')


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username Already Exists')
                return render(request, 'usersTemplate/register.html')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, 'Email Already Exists')
                    return render(request, 'usersTemplate/register.html')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    messages.add_message(request, messages.SUCCESS,
                                         f'Registration Successful Welcome {user.username}')
                    return redirect('user_login')
        else:
            messages.add_message(request, messages.ERROR, 'Password Not Match')
            return render(request, 'usersTemplate/register.html')
    else:
        return render(request, 'usersTemplate/register.html')


def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'pagesTemplate/projects.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, f'Login Successful Welcome {user.username}')
            return redirect('projects')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            return render(request, 'usersTemplate/login.html')
    else:
        return render(request, 'usersTemplate/login.html')


def user_logout(request):
    user = request.user
    logout(request)
    messages.add_message(request, messages.WARNING, f'Log out Successful Good Bye {user.username} ')
    return redirect('user_login')

# Create your views here.
