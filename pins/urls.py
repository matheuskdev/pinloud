from django.urls import path
from . import views

urlpatterns = [
    path(
        'pins/',
        views.PinListCreateView.as_view(),
        name='pin-list'
    ),
    path(
        'pins/<int:pk>',
        views.PinRetrieveUpdateDestroyView.as_view(),
        name='pin-detail'
    ),
    path(
        'pins/<int:pk>/comments/',
        views.PinCommentLikeListView.as_view(),
        name='pin-retrieve'
    ),
]