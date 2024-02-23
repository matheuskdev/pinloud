from rest_framework import serializers
from .models import Like


class LikePinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['user', 'pin', 'created_at']
