from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class PropertyCategory(models.Model):
  name = models.CharField(_("اسم الفئة"), max_length=100)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "فئة عقار"
    verbose_name_plural = "فئات العقارات"

class Property(models.Model):
  name = models.CharField(_("اسم العقار"), max_length=200)
  description = models.TextField(_("الوصف"), blank=True, null=True)
  address = models.TextField(_("العنوان"))
  city = models.CharField(_("المدينة"), max_length=100)
  governorate = models.CharField(_("المحافظة"), max_length=100)
  category = models.ForeignKey(PropertyCategory, on_delete=models.SET_NULL, null=True, verbose_name=_("الفئة"))
  total_units = models.PositiveIntegerField(_("إجمالي الوحدات"), default=0)
  image = models.ImageField(_("صورة العقار"), upload_to='properties/images/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_("المالك"))

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "عقار"
    verbose_name_plural = "العقارات"

class Unit(models.Model):
  class UnitType(models.TextChoices):
    APARTMENT = 'شقة', _('شقة')
    OFFICE = 'مكتب', _('مكتب')
    SHOP = 'محل', _('محل تجاري')
    WAREHOUSE = 'مخزن', _('مخزن')
    PARKING = 'موقف', _('موقف سيارات')
    OTHER = 'أخرى', _('أخرى')

  class UnitStatus(models.TextChoices):
    AVAILABLE = 'متاحة', _('متاحة')
    OCCUPIED = 'مؤجرة', _('مؤجرة')
    MAINTENANCE = 'الصيانة', _('تحت الصيانة')
    INACTIVE = 'غير نشطة', _('غير نشطة')

  property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units', verbose_name=_("العقار"))
  name = models.CharField(_("اسم الوحدة"), max_length=100)
  unit_type = models.CharField(_("نوع الوحدة"), max_length=20, choices=UnitType.choices)
  floor = models.IntegerField(_("الطابق"), default=0)
  area_sqm = models.DecimalField(_("المساحة (متر مربع)"), max_digits=8, decimal_places=2)
  status = models.CharField(_("الحالة"), max_length=20, choices=UnitStatus.choices, default=UnitStatus.AVAILABLE)
  price_monthly = models.DecimalField(_("الإيجار الشهري"), max_digits=10, decimal_places=2)
  notes = models.TextField(_("ملاحظات"), blank=True, null=True)

  def __str__(self):
    return f"{self.property.name} - {self.name}"

  class Meta:
    verbose_name = "وحدة"
    verbose_name_plural = "الوحدات"

class UnitImage(models.Model):
  unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='images')
  image = models.ImageField(upload_to='units/images/')
  caption = models.CharField(_("وصف الصورة"), max_length=255, blank=True)

  def __str__(self):
    return f"صورة - {self.unit.name}"

  class Meta:
    verbose_name = "صورة وحدة"
    verbose_name_plural = "صور الوحدات"

class UnitFeature(models.Model):
  unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='features')
  feature_name = models.CharField(_("الميزة"), max_length=100)

  def __str__(self):
    return self.feature_name

  class Meta:
    verbose_name = "ميزة الوحدة"
    verbose_name_plural = "مزايا الوحدات"