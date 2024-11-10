from django import forms
from .models import Document
import datetime

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['major', 'city', 'country', 'year', 'fname', 'lname', 'advisor', 'f_path']
