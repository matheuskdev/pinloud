from django.urls import path
from . import views

urlpatterns = [
    path(
        'accounts/register/',
        views.UserRegistrationView.as_view(),
        name='user_registration'
        ),
    path(
        'accounts/user/<str:username>/',
        views.UserProfileView.as_view(),
        name=views.UserProfileView.name
    ),
    path(
        'accounts/user/',
        views.UserLoggedView.as_view(),
        name = views.UserLoggedView.name
    ),
]
