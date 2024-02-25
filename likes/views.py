from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework import serializers
from rest_framework.response import Response

from pins.models import Pin

from .models import Like
from .serializers import LikePinSerializer

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like
    serializer_class = LikePinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get(self, request, *args, **kwargs):
        comments = Like.objects.all()
        serializer = LikePinSerializer(comments, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        pin_id = self.kwargs.get('pk')
        return Like.objects.filter(pin_id=pin_id)







class LikePinCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePinSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def perform_create(self, serializer):
        user = self.request.user
        pin_id = self.kwargs.get('pk')
        existing_like = Like.objects.filter(user=user, pin_id=pin_id).first()
        if existing_like:
            # Retornar uma resposta indicando que o Like já existe
            raise serializers.ValidationError(detail="Você já curtiu este Pin.", code=400)
        # Se não existir, criar o novo Like
        serializer.save(user=user, pin_id=pin_id)

""" class LikePinListView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
 """
class LikePinListView(generics.ListCreateAPIView):
    serializer_class = LikePinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pin_id = self.kwargs.get('pk')
        queryset = Like.objects.filter(pin_id=pin_id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        pin_id = self.kwargs.get('pk')
        pin = get_object_or_404(Pin, pk=pin_id)
        serializer.validated_data['pin'] = pin
        serializer.save(user=self.request.user, pin=pin)


""" class LikePinListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        pin_id = self.kwargs.get('pin_id')
        pin = get_object_or_404(Pin, pk=pin_id)
        serializer.save(user=self.request.user)
 """


class LikePinDestroyView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        return Like.objects.get(user=self.request.user, pin=self.get_post())

    def get_post(self):
        return Pin.objects.get(id=self.kwargs['pk'])
