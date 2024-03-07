from rest_framework import serializers

from .models import SavedPin


class SavedPinSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedPin
        fields = ["user", "pin", "created_at"]
