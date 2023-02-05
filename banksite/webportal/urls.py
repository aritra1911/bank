from django.urls import path, URLPattern
from . import views
from typing import List

urlpatterns: List[URLPattern] = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]