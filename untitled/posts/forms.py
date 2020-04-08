from django import forms
from .models import Posts

class ImageForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['image','author','title','body',]
        labels = {
            'image': 'Select a file',
        }
        help_texts = {
            'image': 'max. 42 megabytes',
        }