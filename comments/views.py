from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.response import Response

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)  
        return Response(serializer.data)
    

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment
    serializer_class = CommentSerializer

