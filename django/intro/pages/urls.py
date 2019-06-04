from django.urls import path
from . import views  # 현재 디렉토리(pages)에서 view import

urlpatterns = [
    path('index/', views.index),
    path('hola/', views.hola),
    path('dinner/', views.dinner),
    path('hello/<str:name>/', views.hello),  # <>default: string/ <str:name> == <name>
    path('introduce/<name>/<int:age>/', views.introduce),
    path('times/<int:num1>/<int:num2>', views.times),
    path('circle/<int:radius>', views.circle),
    path('template_language/', views.template_language),
    path('birth/', views.birth),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.lotto),
    path('get/', views.get),
    path('lotto2/', views.lotto2),
    path('picklotto/', views.picklotto),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]