from django.forms import ModelForm
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['header', 'body', 'is_favorite', 'category']
