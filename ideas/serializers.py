from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import Idea


class IdeaModelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Idea
        fields = ["title", "id", "user"]
