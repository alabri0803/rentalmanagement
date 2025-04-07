from django import forms
from django.forms.widgets import DateInput

from .models import Tenant


class HijriDateInput(DateInput):
  input_type = 'date'
  
class TenantForm(forms.ModelForm):
  class Meta:
    model = Tenant
    fields = '__all__'
    widgets = {
      'full_name': forms.TextInput(attrs={'class': 'form-control'}),
      'tenant_type': forms.Select(attrs={'class': 'form-select'}),
      'unit': forms.Select(attrs={'class': 'form-control'}),
      'id_number': forms.TextInput(attrs={'class': 'form-control'}),
      'phone': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'contract_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'contract_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'status': forms.Select(attrs={'class': 'form-select'}),
      'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
    }
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['id_document'].widget.attrs.update({'class': 'form-control', 'accept': 'image/*'})
    self.fields['contract_file'].widget.attrs.update({'class': 'form-control', 'accept': '.pdf'})