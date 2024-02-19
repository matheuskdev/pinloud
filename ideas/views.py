from rest_framework import generics
from .serializers import IdeaModelSerializer
from .models import Idea


class IdeaListCreateView(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaModelSerializer


class IdeaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaModelSerializer
