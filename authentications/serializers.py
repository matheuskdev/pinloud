from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError(detail="Usuário o senha inválido.")

            if not user.check_password(password):
                raise serializers.ValidationError(detail="Senha incorreta.")
        else:
            raise serializers.ValidationError("É necessário preencher email e senha.")

        attrs['user'] = user
        return attrs
