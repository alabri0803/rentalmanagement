from django import forms

from .models import Property, PropertyImage


class PropertyForm(forms.ModelForm):
  class Meta:
    model = Property
    fields = [
      'name', 'type', 'category', 'city', 'address', 
      'description', 'status', 
      'floor_count', 'unit_count',
      'has_parking', 'has_elevator', 
      'latitude', 'longitude',
      'is_active'
    ]
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم العقار'}),
      'type': forms.Select(attrs={'class': 'form-control'}),
      'category': forms.Select(attrs={'class': 'form-control'}),
      'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المدينة'}),
      'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'العنوان الكامل'}),
      'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'وصف إضافي'}),
      'status': forms.Select(attrs={'class': 'form-control'}),
      'floor_count': forms.NumberInput(attrs={'class': 'form-control'}),
      'unit_count': forms.NumberInput(attrs={'class': 'form-control'}),
      'has_parking': forms.CheckboxInput(),
      'has_elevator': forms.CheckboxInput(),
      'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
      'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
      'is_active': forms.CheckboxInput(),
    }
    labels = {
      'name': 'اسم العقار',
      'type': 'نوع العقار',
      'category': 'الفئة',
      'city': 'المدينة',
      'address': 'العنوان',
      'description': 'الوصف',
      'status': 'الحالة',
      'floor_count': 'عدد الطوابق',
      'unit_count': 'عدد الوحدات',
      'has_parking': 'يوجد موقف',
      'has_elevator': 'يوجد مصعد',
      'latitude': 'خط العرض',
      'longitude': 'خط الطول',
      'is_active': 'نشط؟'
    }

class PropertyImageForm(forms.ModelForm):
  class Meta:
    model = PropertyImage
    fields = ['image', 'caption']
    widgets = {
      'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
      'caption': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تعليق على الصورة'}),
    }
    labels = {
      'image': 'الصورة',
      'caption': 'التعليق',
    }