from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from .models import Pin, Like
from .serializers import LikePinSerializer
from rest_framework.permissions import IsAuthenticated


class LikePinCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePinSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pin = self.get_object()
        serializer.save(user=self.request.user, pin=pin)

    def get_object(self):
        return Pin.objects.get(id=self.kwargs['post_id'])


class LikePinDestroyView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePinSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Like.objects.get(user=self.request.user, pin=self.get_post())

    def get_post(self):
        return Pin.objects.get(id=self.kwargs['post_id'])
