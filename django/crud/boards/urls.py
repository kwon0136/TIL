from django.urls import path
from . import views # 현재 디렉토리의 views를 불러온다

#2개 이상의 앱에서, 동일한 url 별명을 구분하기 위해 app_name을 설정한다.
app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    #path('create/', views.create, name='create'),
    path('<int:board_pk>/', views.detail, name='detail'), # variable routing 주소의 일정부분을 변수로 사용한다/ default:string이므로 int로 변환
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/edit/', views.edit, name='edit'),
    #path('<int:pk>/update/', views.update, name='update'),
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:board_pk>/comments/<int:comment_pk>/edit/', views.comments_edit, name='comments_edit'),
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]

# 세번재 인자로 별명을 부여한다.
# --> 주소에 의존하지 않는다.
# --> 주소 변경이 용이하다.(다른곳에서는 별명을 사용하므로 urls.py에서만 변경하면 된다.)