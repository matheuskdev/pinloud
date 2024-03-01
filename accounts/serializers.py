from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'email', 'username', 'password',
            'first_name', 'last_name', 'bio', 'website', 'profile_picture'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'username', 'first_name', 'last_name']

    def validate_email(self, value):
        if self.model.objects.filter(email=value).exists():
            raise serializers.ValidationError('Este e-mail já está em uso.')
        return value

    def validate_username(self, value):
        if self.model.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                'Este nome de usuário já está em uso.'
            )
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance