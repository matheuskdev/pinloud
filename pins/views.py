from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Pin
from .serializers import PinSerializer, PinCommentSerializer


class PinListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinCommentLikeListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pin.objects.all()
    serializer_class = PinCommentSerializer
