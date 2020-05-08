from django.forms import ModelForm, Textarea, TextInput, BooleanField, CheckboxInput, Select
from .models import Note, Category
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['header', 'body', 'is_favorite', 'category']
        widgets = {
            'header': TextInput(),
            'body': SummernoteWidget(),
            'is_favorite': CheckboxInput(),
            'category': Select(),
        }
