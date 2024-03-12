from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.permissions import IsOwnerOrAdmin
from pins.models import Pin

from .models import Like
from .serializers import LikePinSerializer


class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePinSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        pin_id = self.request.data.get("pin")
        pin = get_object_or_404(Pin, pk=pin_id)

        if Like.objects.filter(user=user, pin=pin).exists():
            raise serializers.ValidationError("Você já salvou este pin.")

        serializer.save(user=user, pin=pin)


class LikePinDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePinSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]

    def get_object(self):
        user = self.request.user
        pin = self.get_pin()
        return get_object_or_404(Like, user=user, pin=pin)

    def get_pin(self):
        return get_object_or_404(Pin, id=self.kwargs["pk"])
