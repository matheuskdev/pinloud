from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from pins.models import Pin
from core.permissions import IsOwnerOrAdmin

from .models import SavedPin
from .serializers import SavedPinSerializer


class SavePinView(generics.CreateAPIView):
    serializer_class = SavedPinSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        pin_id = self.kwargs.get('pin_id')
        pin = get_object_or_404(Pin, pk=pin_id)
        
        # Verifica se o Pin já foi salvo pelo usuário
        if SavedPin.objects.filter(user=user, pin=pin).exists():
            return Response(
                {'detail': 'Você já salvou este Pin.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save(user=user, pin=pin)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserSavedPinsView(generics.ListAPIView):
    serializer_class = SavedPinSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return SavedPin.objects.filter(user=user).select_related('pin')


class RemoveSavedPinView(generics.DestroyAPIView):
    queryset = SavedPin.objects.all()
    serializer_class = SavedPinSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        pin_id = self.kwargs.get('pin_id')

        # Verifique se o Pin está salvo pelo usuário
        saved_pin = get_object_or_404(SavedPin, user=user, pin_id=pin_id)
        saved_pin.delete()

        return Response(
            {'message': 'Pin removido dos salvos com sucesso'}, 
            status=status.HTTP_204_NO_CONTENT
        )
