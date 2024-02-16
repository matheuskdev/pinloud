from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('pins.urls')),
    path('api/v1/', include('authentications.urls')),
    path('api/v1/', include('comments.urls')),
    path('api/v1/', include('ideas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
