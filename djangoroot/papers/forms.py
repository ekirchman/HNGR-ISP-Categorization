from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'f_path',
            'year',
            'city',
            'country',
            'major',
            'author',
            'advisor',
            'themes',
        ]
        widgets = {
            'year': forms.TextInput(attrs={'placeholder': 'Year'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
            'major': forms.TextInput(attrs={'placeholder': 'Major or Field'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author Name'}),
            'advisor': forms.TextInput(attrs={'placeholder': 'Advisor Name'}),
            'themes': forms.Textarea(attrs={'placeholder': 'Themes or Keywords', 'rows': 3}),
        }
