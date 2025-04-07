from django import forms

from .models import Property, PropertyImage


class PropertyForm(forms.ModelForm):
  class Meta:
    model = Property
    fields = '__all__'
    widgets = {
      'description': forms.Textarea(attrs={'rows': 4}),
    }

class PropertyImageForm(forms.ModelForm):
  class Meta:
    model = PropertyImage
    fields = ['image', 'caption']