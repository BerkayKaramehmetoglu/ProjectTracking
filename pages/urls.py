from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('', views.pages, name='pages')
]