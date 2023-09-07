from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from . import views




urlpatterns = [
    path('index/', views.index),
    path('create/', views.create),
]
