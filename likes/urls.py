from django.urls import path

from . import views

urlpatterns = [
    path(
        "likes/<int:pk>/",
        views.LikePinDestroyView.as_view(),
        name="like_pin_delete",
    ),
    path(
        "likes/",
        views.LikeListCreateView.as_view(),
        name="like_pin_list_create",
    ),
]
