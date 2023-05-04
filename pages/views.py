from django.http.response import HttpResponse
from django.shortcuts import render


def pages(request):
    return render(request, 'pagesTemplate/pages.html')


def homepage(request):
    return render(request, 'pagesTemplate/home.html')
# Create your views here.
