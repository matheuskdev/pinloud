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


class IdeaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaModelSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin, ]
