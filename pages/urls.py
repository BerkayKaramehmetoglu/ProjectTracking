from django.urls import path
from . import views

urlpatterns = [
    path('myproject/', views.myprojects, name='myproject'),
    path('projects/', views.projects, name='projects'),
    path('register/', views.register, name='register'),
    path('', views.pages, name='pages')
]