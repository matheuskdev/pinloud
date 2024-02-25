from django.db import models
from accounts.models import User
from ideas.models import Idea


class Pin(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='pins/')
    user = models.ForeignKey(
        User,
        related_name='pins',
        on_delete=models.CASCADE
    )
    ideas =  models.ManyToManyField(Idea, related_name='pins')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title
