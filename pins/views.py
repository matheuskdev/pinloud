from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly, 
)
from core.permissions import IsOwnerOrAdmin

from .models import Pin
from .serializers import PinSerializer, PinAllDataSerializer


class PinListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin, ]
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinAllDataListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Pin.objects.all()
    serializer_class = PinAllDataSerializer


class PinAllDataRetriveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Pin.objects.all()
    serializer_class = PinAllDataSerializer
