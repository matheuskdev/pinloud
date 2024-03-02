from django.urls import path
from . import views

urlpatterns = [
    path(
        'accounts/register/',
        views.UserRegistrationView.as_view(),
        name=views.UserRegistrationView.name
    ),
    path('accounts/user/<str:username>/',
         views.UserProfileView.as_view(),
         name=views.UserProfileView.name)
]
