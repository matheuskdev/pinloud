import json
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import serializers

from accounts.serializers import UserSerializer
from comments.serializers import CommentSerializer
from ideas.serializers import IdeaModelSerializer
from likes.serializers import LikePinSerializer

from .models import Pin


class PinSerializer(serializers.ModelSerializer):
    ideas = IdeaModelSerializer(many=True, read_only=True)

    class Meta:
        model = Pin
        fields = (
            "id",
            "title",
            "description",
            "image",
            "ideas",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        ideas_data = self.context.get("request").data.getlist("ideas", [])
        string_json = ideas_data[0]
        list_dict = json.loads(string_json)
        list_value = [item['id'] for item in list_dict]
        pin = Pin.objects.create(**validated_data)
        pin.ideas.set(list_value)
        return pin

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user"] = UserSerializer(instance.user).data
        return representation


class PinAllDataSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(
        many=True,
        read_only=True,
    )
    likes = LikePinSerializer(many=True, read_only=True)
    total_likes = serializers.SerializerMethodField(read_only=True)
    ideas = IdeaModelSerializer(many=True, read_only=True)

    class Meta:
        model = Pin
        fields = [
            "id",
            "title",
            "description",
            "image",
            "user",
            "comments",
            "likes",
            "ideas",
            "total_likes",
        ]

    def get_total_likes(self, object) -> float:
        total_likes = object.likes.count()
        return round(total_likes, 1) if total_likes else None


class PinUserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Pin
        fields = (
            "id",
            "image",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Garanta que a URL da imagem seja absoluta
        if "image" in representation and representation["image"]:
            request = self.context.get("request", None)
            if request is not None:
                representation["image"] = request.build_absolute_uri(
                    instance.image.url
                )
            else:
                current_site = get_current_site(None)
                domain = current_site.domain
                representation["image"] = (
                    f"http://{domain}{instance.image.url}"
                )
        return representation
