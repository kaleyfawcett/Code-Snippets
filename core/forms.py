from django import forms
# from .models import Tag
from .models import CodeSnippet

class SnippetForm(forms.ModelForm):
    tag_names = forms.CharField(label="Tags", help_text="Enter tags separated by spaces.", widget=forms.TextInput(attrs={'class': 'pa2 f4 w-50'}))

    class Meta:
        model = CodeSnippet
        fields = [
            'user',
            'title',
            'language',
            'code_body',
            'is_public',
            'parent',

        ]

# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = [
#             'tag',
#         ]        