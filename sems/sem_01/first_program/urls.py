from django.urls import path

from . import views
from .views import index, about


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
]

