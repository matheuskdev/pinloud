from django.urls import path
from . import views

urlpatterns = [
    path(
        'ideas/',
        views.IdeaListCreateView.as_view(),
        name='idea-list'
    ),
    path(
        'ideas/<int:pk>/',
        views.IdeaRetrieveUpdateDestroyView.as_view(),
        name='idea-detail'
    ),
]