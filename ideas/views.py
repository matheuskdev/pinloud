from rest_framework import generics, permissions

from .serializers import IdeaModelSerializer
from .models import Idea


class IdeaListCreateView(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)    


class IdeaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaModelSerializer
