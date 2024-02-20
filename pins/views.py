from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Pin
from .serializers import PinSerializer, PinCommentSerializer
from rest_framework.permissions import IsAuthenticated


class PinListCreateView(
    #LoginRequiredMixin, 
    generics.ListCreateAPIView
):
    permission_classes = (IsAuthenticated,)
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinRetrieveUpdateDestroyView(
    #LoginRequiredMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinListView(generics.ListAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinCommentSerializer