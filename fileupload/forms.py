from .models import FileUpload
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('attachment_file', )