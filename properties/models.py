from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Property(models.Model):
  name = models.CharField(max_length=255, verbose_name=_("اسم العقار"))
  address = models.TextField(verbose_name=_("العنوان"))
  city = models.CharField(max_length=100, verbose_name=_("المدينة"))
  owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_("المالك"))
  description = models.TextField(blank=True, null=True, verbose_name=_("الوصف"))
  latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name=_("خط العرض"))
  longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name=_("خط الطول"))
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Unit(models.Model):
  UNIT_TYPE_CHOICES = [
    ('apartment', _('شقة')),
    ('office', _('مكتب')),
    ('shop', _('محل تجاري')),
    ('warehouse', _('مخزن')),
    ('parking', _('موقف سيارات'))
  ]
  STATUS_CHOICES = [
    ('available', _('متاح')),
    ('rented', _('مؤجرة')),
    ('maintenance', _('صيانة'))
  ]
  property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units', verbose_name=_("العقار"))
  name = models.CharField(max_length=100, verbose_name=_("اسم الوحدة"))
  unit_type = models.CharField(max_length=20, choices=UNIT_TYPE_CHOICES, verbose_name=_("نوع الوحدة"))
  floor = models.IntegerField(verbose_name=_("الطابق"))
  area = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("المساحة بالمتر"))
  rooms = models.PositiveIntegerField(default=0, verbose_name=_("عدد الغرف"))
  bathrooms = models.PositiveIntegerField(default=0, verbose_name=_("عدد الحمامات"))
  furnished = models.BooleanField(default=False, verbose_name=_("مفروشة"))
  price_monthly = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("الإيجار الشهري"))
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name=_("الحالة"))
  
  def __str__(self):
    return f"{self.name} - {self.property.name}"
    
class UnitImage(models.Model):
  unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='images', verbose_name=_("الوحدة"))
  image = models.ImageField(upload_to='unit_images/', verbose_name=_("الصورة"))
  
  def __str__(self):
    return f"صورة {self.unit.name}"

class Feature(models.Model):
  unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='features', verbose_name=_("الوحدة"))
  feature = models.CharField(max_length=255, verbose_name=_("الميزة"))

  def __str__(self):
    return f"{self.feature} - {self.unit.name}"