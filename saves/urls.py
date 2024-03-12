from django.urls import path

from . import views

urlpatterns = [
    path(
        "saved_pins/",
        views.SavePinListCreateView.as_view(),
        name="saved_pin_list_create",
    ),
    path(
        "saved_pins/<int:pk>",
        views.SavedPinDestroyView.as_view(),
        name="saved_pin_destroy",
    ),
]
