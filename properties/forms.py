from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
  class Meta:
    model = Property
    fields = '__all__'
    widgets = {
      'description': forms.Textarea(attrs={'rows': 4}),
      'notes': forms.Textarea(attrs={'rows': 2}),
    }