from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response

from pins.models import Pin
from pins.serializers import PinUserSerializer

from .serializers import UserEditSerializer, UserRegistrationSerializer, UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    """View for registration of users from  a pin."""

    name = "user_registration"
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileView(generics.RetrieveAPIView):
    name = "user_profile"

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(username=kwargs["username"])
        user_serializer = UserSerializer(user)
        pins = Pin.objects.filter(user=user)
        pins_serializer = PinUserSerializer(pins, many=True)
        return Response(
            {"user": user_serializer.data, "pins": pins_serializer.data}
        )


class UserLoggedView(generics.RetrieveAPIView):
    name = "user_logged"

    def get(self, request, *args, **kwargs):
        user = request.user
        user_serializer = UserSerializer(
            user, many=False, context={"request": request}
        ).data
        pins = Pin.objects.filter(user=user)
        pins_data = PinUserSerializer(
            pins, many=True, context={"request": request}
        ).data

        return Response({"user": user_serializer, "pins": pins_data})


class UserUpdateView(generics.UpdateAPIView):
    """View for editing the user profile."""
    name = "user_edit"
    serializer_class = UserEditSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)