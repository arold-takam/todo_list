from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),  # La page d'accueil
    path('Add_Task/', views.Add_Task, name='Add_Task'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('modify_task/<int:id>/', views.Modify_Task, name='Modify_Task'),  # Route pour la modification
]
