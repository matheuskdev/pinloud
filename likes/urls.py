from django.urls import path
from . import views

urlpatterns = [
    path(
        'likes/<int:pk>/',
        views.LikePinDestroyView.as_view(),
        name='like_pin_delete'
    ),
    path(
        'likes/',
        views.LikePinListView.as_view(),
        name='like_pin_list'
    ),
    path(
        'pins/<int:pk>/likes/',
        views.LikePinCreateView.as_view(),
        name='like_pin_create'
        ),
path('pins/<int:pk>/likes/', views.LikePinListView.as_view(), name='like_pin_list')

]
