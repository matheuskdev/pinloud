from rest_framework import serializers

from accounts.serializers import UserSerializer
from accounts.models import User
from comments.serializers import CommentSerializer
from ideas.serializers import IdeaModelSerializer
from likes.serializers import LikePinSerializer

from .models import Pin


class PinSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True
    )

    class Meta:
        model = Pin
        fields = (
            'id', 'title', 'description', 'image', 'ideas', 'user',
            'created_at', 'updated_at'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        return representation


class PinAllDataSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True,)
    likes = LikePinSerializer(many=True, read_only=True)
    total_likes = serializers.SerializerMethodField(read_only=True)
    ideas = IdeaModelSerializer(many=True, read_only=True)
                           
    class Meta:
        model = Pin
        fields = [
            'id', 'title', 'description', 
            'user', 'comments', 'likes','ideas', 'total_likes'
        ]

    def get_total_likes(self, object) -> float:
        total_likes = object.likes.count()
        return round(total_likes, 1) if total_likes else None
