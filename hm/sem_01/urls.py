from django.urls import path

from . import views

urlpatterns = [
    path('sem_01/', views.index),
    path('sem_01/about/', views.about),
]

