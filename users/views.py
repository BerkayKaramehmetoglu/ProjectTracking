from django.http.response import HttpResponse


def users(request):
    return HttpResponse("Hello, world. You're at the users index.")
# Create your views here.
