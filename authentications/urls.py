from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,\
                                            TokenRefreshView, \
                                            TokenVerifyView


urlpatterns = [
    path(
        'authentications/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'authentications/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
    'authentications/token/verify/',
    TokenVerifyView.as_view(),
    name='token_verify'
    )
]
