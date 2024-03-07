from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "bio",
            "website",
            "profile_picture",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "username",
        ]

    def validate_email(self, value):
        if self.Meta.model.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este e-mail já está em uso.")
        return value

    def validate_username(self, value):
        if self.Meta.model.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Este nome de usuário já está em uso."
            )
        return value

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Garanta que a URL da imagem seja absoluta
        if (
            "profile_picture" in representation
            and representation["profile_picture"]
        ):
            request = self.context.get("request", None)
            if request is not None:
                representation["profile_picture"] = request.build_absolute_uri(
                    instance.profile_picturege.url
                )
            else:
                current_site = get_current_site(None)
                domain = current_site.domain
                representation["profile_picture"] = (
                    f"http://{domain}{instance.profile_picture.url}"
                )
        return representation
