from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import MinLengthValidator
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O campo de email deve ser preenchido.")

        # Normaliza o endereço de email (minúsculas)
        email = self.normalize_email(email)

        # Cria um novo usuário com os campos fornecidos
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        # Salva o usuário no banco de dados usando o banco de dados padrão
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Define valores padrão para um superusuário
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        # Cria um superusuário usando o método create_user
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # Campos para o modelo de usuário
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=18,
        unique=True,
        validators=[
            MinLengthValidator(
                limit_value=4,
                message="O nome de usuário deve ter no mínimo 4 caracteres.",
            )
        ],
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True, null=True, max_length=1012)
    website = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )

    # Campos de status do usuário
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Campos de data e hora
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Gerenciador para o modelo de usuário
    objects = CustomUserManager()

    # Campos necessários para autenticação
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
