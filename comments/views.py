from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        pin_id = self.kwargs.get('pk')
        return Comment.objects.filter(pin_id=pin_id)


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]