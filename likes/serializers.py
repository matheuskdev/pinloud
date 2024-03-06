from rest_framework import serializers
from .models import Like

class LikePinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['pin', 'created_at']
