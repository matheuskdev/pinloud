from django.db import models
from django.contrib.auth import get_user_model

from pins.models import Pin


class Like(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    pin = models.ForeignKey(
        Pin,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            unique_together = ('user', 'pin')

    def __str__(self) -> str:
        return f"{self.user.username.title()} Curtiu {self.pin.title.title()}"
