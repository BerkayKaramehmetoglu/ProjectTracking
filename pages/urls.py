from django.urls import path
from . import views

urlpatterns = [
    path('myproject/', views.myproject, name='myproject'),
    path('myproject/<str:project_name>', views.projectname, name='projectname'),
    path('projects/', views.projects, name='projects'),
    path('register/', views.register, name='register'),
    path('', views.pages, name='pages')
]