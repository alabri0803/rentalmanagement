from django.db import models


class Property(models.Model):
  PROERTY_TYPES = [
    ('apartment', 'شقة'),
    ('office', 'مكتب'),
    ('shop', 'محل'),
    ('warehouse', 'مخزن'),
    ('parking', 'موقف سيارات')
  ]
  name = models.CharField(max_length=200, verbose_name='اسم العقار')
  description = models.TextField(blank=True, null=True, verbose_name='الوصف')
  property_type = models.CharField(max_length=20, choices=PROERTY_TYPES, verbose_name='نوع العقار')
  area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='المساحة (م2)')
  floor_number = models.IntegerField(null=True, blank=True, verbose_name='رقم الطابق')
  rent_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قيمة الإيجار الشهري')
  is_available = models.BooleanField(default=True, verbose_name='متاح')
  owner_share = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='نسبة المالك')
  investor_share = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='نسبة المستثمر')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الاإضافة')



  def __str__(self):
    return f"{self.name} - {self.get_property_type_display()}"