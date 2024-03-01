from django.urls import path
from . import views

urlpatterns = [
    path(
        'accounts/register/',
        views.UserRegistrationView.as_view(),
        name=views.UserRegistrationView.name
    ),
]
