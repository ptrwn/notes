from django.forms import ModelForm, Textarea, TextInput, BooleanField, CheckboxInput, Select
from .models import Note, Category


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['header', 'body', 'is_favorite', 'category']
        widgets = {
            'header': TextInput(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'is_favorite': CheckboxInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
        }


class RegLogForm(ModelForm):
    class Meta:
        pass