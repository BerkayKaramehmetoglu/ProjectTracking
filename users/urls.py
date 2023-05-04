from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'), #buraya user nameleri gelıcek
    path('', views.users, name='users'),
]