from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly
)
from core.permissions import IsOwnerOrAdmin

from .serializers import IdeaModelSerializer
from .models import Idea


class IdeaListCreateView(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]   

    def perform_create(self, serializer):
        # Atribui automaticamente o usuário da solicitação ao objeto
        serializer.save(user=self.request.user)


class IdeaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaModelSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin, ]
