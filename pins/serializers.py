from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Pin

class PinSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Pin
        fields = (
            'id', 'title', 'description', 'image', 'user',
            'created_at', 'updated_at'
        )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.pop('user', None)
        pin = Pin.objects.create(user=user, **validated_data)
        return pin
