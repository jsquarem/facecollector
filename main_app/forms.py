from django import forms
from .models import Face, Picture, Tag

class FaceForm(forms.ModelForm):
  class Meta:
    model = Face
    fields = ('name', 'age', 'golden_ratio', 'gender')

    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'age': forms.TextInput(attrs={'class': 'form-control'}),
      'golden_ratio': forms.TextInput(attrs={'class': 'form-control'}),
      'gender': forms.Select(attrs={'class': 'form-control'})
    }

class PictureForm(forms.ModelForm):
  class Meta:
    model = Picture
    fields = ('url',)

    widgets = {
      'url': forms.URLInput(attrs={'class': 'form-control'})
    }

class TagForm(forms.ModelForm):
  class Meta:
    model = Tag
    fields = ('name',)

    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'})
    }
