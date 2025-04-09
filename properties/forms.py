from django import forms

from .models import Feature, Property, Unit, UnitImage


class PropertyForm(forms.ModelForm):
  class Meta:
    model = Property
    fields = ['name', 'city', 'address', 'owner', 'description']
    widgets = {
      'description': forms.Textarea(attrs={'rows': 3}),
      'latitude': forms.NumberInput(attrs={'step': 'any'}),
      'longitude': forms.NumberInput(attrs={'step': 'any'}),
    }

class UnitForm(forms.ModelForm):
  class Meta:
    model = Unit
    fields = '__all__'

class FeatureForm(forms.ModelForm):
  class Meta:
    model = Feature
    fields = ["unit", "feature"]

class UnitImageForm(forms.ModelForm):
  class Meta:
    model = UnitImage
    fields = ["unit", "image"]