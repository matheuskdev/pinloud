from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserSerializer
from pins.serializers import PinSerializer, PinUserSerializer
from pins.models import Pin

class UserRegistrationView(generics.CreateAPIView):
    name = 'user_registration'
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileView(generics.RetrieveAPIView):
    name='user_profile'
    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(username=kwargs['username'])
        user_serializer = UserSerializer(user)
        pins = Pin.objects.filter(user=user)
        pins_serializer = PinUserSerializer(pins, many=True)
        return Response({
            'user': user_serializer.data,
            'pins': pins_serializer.data
        })

class UserLoggedView(generics.RetrieveAPIView):
    name = 'user_logged'

    def get(self, request, *args, **kwargs):
        user = request.user
        user_serializer = UserSerializer(
            user,
            many=False,
            context={'request': request}
        ).data
        pins = Pin.objects.filter(user=user)
        pins_data = PinUserSerializer(
            pins,
            many=True,
            context={'request': request}
        ).data
        
        return Response({
            'user': user_serializer,
            'pins': pins_data
        })