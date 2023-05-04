from django.http.response import HttpResponse


def pages(request):
    return HttpResponse("Hello, world. You're at the pages index.")
# Create your views here.
