from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:movie_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
]