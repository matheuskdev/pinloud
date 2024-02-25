from django.db import models
from django.contrib.auth import get_user_model

from pins.models import Pin


class SavedPin(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pin = models.ForeignKey(
        Pin, on_delete=models.CASCADE, related_name='saves'
    ) 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'pin')

    def __str__(self):
        return f"{self.user.username} salvou o Pin: {self.pin.title}"