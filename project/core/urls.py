from django.urls import path
from . import views

urlpatterns = [
    path('', views.group),
    path('<str:group_name>/', views.index),
]