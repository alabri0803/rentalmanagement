from django import forms
from django.forms.models import inlineformset_factory
from django.utils.translation import gettext_lazy as _

from .models import Property, Unit, UnitFeature, UnitImage


class PropertyForm(forms.ModelForm):
  class Meta:
    model = Property
    fields = [
      "name", "description", "address", "city", "governorate", 
      "category", "total_units", "image"
    ]
    labels = {
      "name": _("اسم العقار"),
      "description": _("الوصف"),
      "address": _("العنوان"),
      "city": _("المدينة"),
      "governorate": _("المحافظة"),
      "category": _("الفئة"),
      "total_units": _("إجمالي الوحدات"),
      "image": _("صورة العقار"),
    }
    widgets = {
      "description": forms.Textarea(attrs={"rows": 3, 'dir': 'rtl'}),
      "address": forms.Textarea(attrs={"rows": 2, 'dir': 'rtl'}),
    }

class UnitForm(forms.ModelForm):
  class Meta:
    model = Unit
    fields = [
      "property", "name", "unit_type", "floor", "area_sqm",
      "status", "price_monthly", "notes"
    ]
    labels = {
      "property": _("العقار"),
      "name": _("اسم الوحدة"),
      "unit_type": _("نوع الوحدة"),
      "floor": _("الطابق"),
      "area_sqm": _("المساحة (متر مربع)"),
      "status": _("الحالة"),
      "price_monthly": _("الإيجار الشهري"),
      "notes": _("ملاحظات"),
    }
    widgets = {
      "notes": forms.Textarea(attrs={"rows": 2, 'dir': 'rtl'}),
    }

class UnitImageForm(forms.ModelForm):
  class Meta:
    model = UnitImage
    fields = ["image", "caption"]
    labels = {
      "image": _("الصورة"),
      "caption": _("الوصف"),
    }
    widgets = {
      "caption": forms.TextInput(attrs={'dir': 'rtl'}),
    }

class UnitFeatureForm(forms.ModelForm):
  class Meta:
    model = UnitFeature
    fields = ["feature_name"]
    labels = {
      "feature_name": _("الميزة"),
    }
    widgets = {
      "feature_name": forms.TextInput(attrs={'dir': 'rtl', 'placeholder': _('مثال: غسالة')}),
    }

UnitImageFormSet = inlineformset_factory(
  parent_model=Unit,
  model=UnitImage,
  form=UnitImageForm,
  extra=2,
  can_delete=True
)

UnitFeatureFormSet = inlineformset_factory(
  parent_model=Unit,
  model=UnitFeature,
  form=UnitFeatureForm,
  extra=3,
  can_delete=True
)