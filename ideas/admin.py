from django.contrib import admin
from .models import Idea


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    fields = ('title', 'user', 'created_at')
    search_fields = ('title', 'user', 'created_at')
    ordering = ('title',)
    readonly_fields = ('created_at',)
