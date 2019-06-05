from django.urls import path
from . import views # 현재 디렉토리의 views를 불러온다

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
]