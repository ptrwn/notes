from django.forms import ModelForm, TextInput, CheckboxInput, Select, inlineformset_factory
from .models import Note, Category
from django_summernote.widgets import SummernoteWidget
from django.utils.translation import gettext_lazy as _


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {'name': TextInput(),}
        error_messages = {
            'name': {
                'unique': _("This category already exists, must be unique."), }}


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['header', 'body', 'is_favorite', 'category']
        labels = {'body': _('Content'), }

        widgets = {
            'header': TextInput(),
            'body': SummernoteWidget(),
            'is_favorite': CheckboxInput(),
            'category': Select(),
        }


# todo: merge forms into
# NoteFormSet = inlineformset_factory(Category, Note, fields=('category', ))
