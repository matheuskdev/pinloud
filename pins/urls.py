from django.urls import path
from . import views

urlpatterns = [
    path(
        'pins/',
        views.PinListCreateView.as_view(),
        name='pin_list'
    ),
    path(
        'pins/<int:pk>/',
        views.PinRetrieveUpdateDestroyView.as_view(),
        name='pin_detail'
    ),
    path(
        'pins/<int:pk>/all/',
        views.PinAllDataRetriveView.as_view(),
        name='pin_all_data_retrive'
    ),
    path(
        'pins/all_data/',
        views.PinAllDataListView.as_view(),
        name='pin_all_data'
    )
]
