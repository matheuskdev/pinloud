from django.db import models
from accounts.models import User


class Idea(models.Model):
    title = models.CharField(max_length=250)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ideas'
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
