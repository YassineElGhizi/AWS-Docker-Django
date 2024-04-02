from django.contrib import admin

from amazon_learning.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "note", "created_at", "updated_at")
