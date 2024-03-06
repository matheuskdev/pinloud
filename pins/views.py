from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly, 
)

from django_filters.rest_framework import DjangoFilterBackend

from core.permissions import IsOwnerOrAdmin

from .filters import PinFilter
from .models import Pin
from .serializers import PinSerializer, PinAllDataSerializer


class PinListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PinFilter
    
    def perform_create(self, serializer):
        # Atribui automaticamente o usuário da solicitação ao objeto
        serializer.save(user=self.request.user)

class PinRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin, ]
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinAllDataListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Pin.objects.all()
    serializer_class = PinAllDataSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PinFilter


class PinAllDataRetriveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Pin.objects.all()
    serializer_class = PinAllDataSerializer
