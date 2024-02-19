from django.urls import path
from . import views

urlpatterns = [
    path(
        'pins/',
        views.PinListCreateView.as_view(),
        name='pin-list'
    ),
    path(
        'pins/<int:pk>/like',
        views.PinRetrieveUpdateDestroyView.as_view(),
        name='pin-detail'
    ),
    path(
        'pins/<int:pk>/',
        views.LikePinListCreateView.as_view(),
        name='like-pin-list'
    ),
    path(
        'pins/<int:pk>/like',
        views.LikePinDestroyView.as_view(),
        name='like-pin-delete'
    ),
    path(
        'pins/<int:pk>/comments/',
        views.PinRetriveView.as_view(),
        name='pin-retrieve'
    ),

]