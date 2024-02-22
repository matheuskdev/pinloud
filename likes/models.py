from django.db import models

from accounts.models import User
from pins.models import Pin


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    pin = models.ForeignKey(
        Pin,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)
