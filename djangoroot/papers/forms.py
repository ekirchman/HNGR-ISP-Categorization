from django import forms
from .models import Document
import datetime

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['language', 'major', 'city', 'pub_date', 'fname', 'lname', 'f_path']
