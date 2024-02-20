from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Pin
from accounts.models import User
from comments.serializers import CommentSerializer
from likes.serializers import LikePinSerializer



class PinSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Pin
        fields = (
            'id', 'title', 'description', 'image', 'user',
            'created_at', 'updated_at'
        )
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        return representation



class PinCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)  # Use o related_name 'comments' aqui
    likes = LikePinSerializer(many=True, read_only=True)

    class Meta:
        model = Pin
        fields = ['id', 'title', 'description', 'user', 'comments', 'likes']