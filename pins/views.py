from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from .models import Pin
from .serializers import PinSerializer


class PinListCreateView(generics.ListCreateAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinRetrieveUpdateDestroyView(

    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
