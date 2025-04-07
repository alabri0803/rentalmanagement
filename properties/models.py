from django.db import models


class Property(models.Model):
  PROERTY_TYPES = [
    ('سكني', 'سكني'),
    ('تجاري', 'تجاري'),
    ('سكني تجاري', 'سكني تجاري'),
    ('مبني إداري', 'مبني إداري'),
  ]
  name = models.CharField(max_length=200, verbose_name='اسم العقار')
  type = models.CharField(max_length=50, choices=PROERTY_TYPES, verbose_name='نوع العقار')
  address = models.CharField(max_length=300, verbose_name='العنوان')
  city = models.CharField(max_length=100, verbose_name='المدينة')
  description = models.TextField(blank=True, null=True, verbose_name='الوصف التفصيلي')

  num_apartments = models.PositiveIntegerField(default=0, verbose_name='عدد الشقق')
  num_offices = models.PositiveIntegerField(default=0, verbose_name='عدد المكاتب')
  num_shops = models.PositiveIntegerField(default=0, verbose_name='عدد المحلات')
  num_stores = models.PositiveIntegerField(default=0, verbose_name='عدد المخازن')
  num_parkings = models.PositiveIntegerField(default=0, verbose_name='عدد المواقف')

  image = models.ImageField(upload_to='properties/', blank=True, null=True, verbose_name='صورة العقار')
  floor_plan = models.FileField(upload_to='floor_plans/', blank=True, null=True, verbose_name='مخطط الطوابق')
  notes = models.TextField(blank=True, null=True, verbose_name='ملاحظات إضافية')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

  def __str__(self):
    return self.name