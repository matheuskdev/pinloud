from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from core.permissions import IsOwnerOrAdmin
from pins.models import Pin

from .models import Like
from .serializers import LikePinSerializer


class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like
    serializer_class = LikePinSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get(self, request, *args, **kwargs):
        comments = Like.objects.all()
        serializer = LikePinSerializer(comments, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        pin_id = self.kwargs.get('pk')
        return Like.objects.filter(pin_id=pin_id)


class LikePinDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePinSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]

    def get_object(self):
        user = self.request.user
        pin = self.get_pin()
        return get_object_or_404(Like, user=user, pin=pin)

    def get_pin(self):
        return get_object_or_404(Pin, id=self.kwargs['pk'])
