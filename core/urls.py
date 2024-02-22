from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="PinLoud API",
      default_version='v1',
      description="Endpoints da API PinLoud",
      terms_of_service="https://www.google.com/",
      contact=openapi.Contact(email="matheuskdev@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
   path('admin/', admin.site.urls),

   path('api/v1/', include('authentications.urls')),
   path('api/v1/', include('comments.urls')),
   path('api/v1/', include('ideas.urls')),
   path('api/v1/', include('likes.urls')),
   path('api/v1/', include('pins.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
