from django.urls import path
from . import views

urlpatterns = [
    path('indes/', views.index),
    path('photo/', views.photo)
]
