from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path('authentications/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
