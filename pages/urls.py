from django.urls import path
from . import views

urlpatterns = [
    path('myproject/', views.myprojects, name='myproject'),
    path('projects/', views.projects, name='projects'),
    path('project-update/<int:id>', views.update, name='project_update'),
    path('project-owner-list/', views.owner_list, name='owner_list'),
    path('myproject/<int:id>', views.delete, name='project_delete'),
    path('authorize/', views.authorized, name='authorized'),
]