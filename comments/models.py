from django.db import models
from accounts.models import User
from pins.models import Pin

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    pin = models.ForeignKey(Pin, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.comment