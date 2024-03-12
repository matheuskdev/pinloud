from django.contrib import admin

from .models import SavedPin


@admin.register(SavedPin)
class SavadPinAdmin(admin.ModelAdmin):
    fields = (
        "user",
        "pin",
        "created_at",
    )
    search_fields = (
        "pin",
        "user",
        "created_at",
    )
    ordering = ("pin",)
    readonly_fields = ("created_at",)
