from rest_framework import generics, permissions

from .models import Pin
from .serializers import PinSerializer, PinCommentSerializer


class PinListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinCommentLikeListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Pin.objects.all()
    serializer_class = PinCommentSerializer
