from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.permissions import IsOwnerOrAdmin
from pins.models import Pin

from .models import SavedPin
from .serializers import SavedPinSerializer


class SavePinListCreateView(generics.ListCreateAPIView):
    serializer_class = SavedPinSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        pin_id = self.kwargs.get("pin_id")
        pin = get_object_or_404(Pin, pk=pin_id)

        # Verifica se o Pin já foi salvo pelo usuário
        if SavedPin.objects.filter(user=user, pin=pin).exists():
            return Response(
                {"detail": "Você já salvou este Pin."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save(user=user, pin=pin)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        return SavedPin.objects.filter(user=user).select_related("pin")


class SavedPinDestroyView(generics.RetrieveDestroyAPIView):
    queryset = SavedPin.objects.all()
    serializer_class = SavedPinSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrAdmin,
    ]

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        pin_id = self.kwargs.get("pk")

        try:
            saved_pin = SavedPin.objects.get(user=user, pin_id=pin_id)
        except SavedPin.DoesNotExist:
            raise Response(
                {"detail": "Pin não encontrado nos salvos deste usuário."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        self.check_object_permissions(request, saved_pin)

        saved_pin.delete()

        return Response(
            {"message": "Pin removido dos salvos com sucesso"},
            status=status.HTTP_204_NO_CONTENT,
        )
