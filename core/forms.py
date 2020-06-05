from django import forms
from .models import Tag
from .models import CodeSnippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = CodeSnippet
        fields = [
            'user',
            'title',
            'language',
            'code_body',
            'is_public',
            'parent',
            'tags',

        ]

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            'tag',
        ]        