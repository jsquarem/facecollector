from django import forms
from .models import Face

class FaceForm(forms.ModelForm):
  class Meta:
    model = Face
    fields = ('name', 'age', 'hotness')

    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'age': forms.TextInput(attrs={'class': 'form-control'}),
      'hotness': forms.TextInput(attrs={'class': 'form-control'})

    }
