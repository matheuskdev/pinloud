from django.urls import path
from . import views

urlpatterns = [
    path(
        'pins/<int:pk>/like/',
        views.LikePinCreateView.as_view(),
        name='like-pin-create'
    ),
    path(
        'pins/<int:pk>/like',
        views.LikePinDestroyView.as_view(),
        name='like-pin-delete'
    ),
]
