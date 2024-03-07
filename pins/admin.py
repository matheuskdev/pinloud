from django.contrib import admin

from .models import Pin


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created_at", "updated_at")
