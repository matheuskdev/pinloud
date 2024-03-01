from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer

class UserRegistrationView(generics.CreateAPIView):
    name = 'user_registration'
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
