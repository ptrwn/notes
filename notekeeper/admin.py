from django.contrib import admin
from .models import Note, Category
from django_summernote.admin import SummernoteModelAdmin


class NoteAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

admin.site.register(Note, NoteAdmin)
admin.site.register(Category)
