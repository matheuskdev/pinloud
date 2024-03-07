import django_filters

from .models import Pin


class PinFilter(django_filters.FilterSet):
    class Meta:
        model = Pin
        fields = {
            "title": ["icontains"],
            "description": ["icontains"],
            "user__username": ["icontains"],
            "ideas": ["exact"],
        }
