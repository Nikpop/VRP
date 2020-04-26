from django import forms
from .models import Posts
from django.utils.translation import gettext_lazy as _

class ImageForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['image','author','title','body','posx', 'posy','posz',]
        labels = {
            'image': _('Select a file'),
        }   
        help_texts = {
            'image': 'max. 42 megabytes',
        }