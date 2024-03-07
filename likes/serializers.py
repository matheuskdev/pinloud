from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import Like


class LikePinSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ["user", "pin", "created_at"]
