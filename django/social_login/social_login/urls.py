from django.contrib import admin
from django.urls import path, include
import login.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login.views.login, name='login'),
    path('accounts/', include('allauth.urls')),
    path('upload/', login.views.upload, name='upload')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)