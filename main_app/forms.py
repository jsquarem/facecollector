from django import forms
from .models import Face, Picture

class FaceForm(forms.ModelForm):
  class Meta:
    model = Face
    fields = ('name', 'age', 'hotness', 'gender')

    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'age': forms.TextInput(attrs={'class': 'form-control'}),
      'hotness': forms.TextInput(attrs={'class': 'form-control'}),
      'gender': forms.Select(attrs={'class': 'form-control'})
    }

class PictureForm(forms.ModelForm):
  class Meta:
    model = Picture
    fields = ('url',)

    widgets = {
      'url': forms.URLInput(attrs={'class': 'form-control'})
    }
