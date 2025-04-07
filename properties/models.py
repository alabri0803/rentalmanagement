from django.db import models

PROERTY_TYPES = [
  ('سكني', 'سكني'),
  ('تجاري', 'تجاري'),
  ('سكني تجاري', 'سكني تجاري'),
  ('مبني إداري', 'مبني إداري'),
]
PROPERTY_CATEGORIES = [
  ('عمارة', 'عمارة'),
  ('برج', 'برج'),
  ('مركز تجاري', 'مركز تجاري'),
  ('فيلا', 'فيلا'),
  ('سكن موظفين', 'سكن موظفين')
]
OCCUPANCY_STATUS = [
  ('مشغول', 'مشغول'),
  ('شاغر', 'شاغر')
]
class Property(models.Model):
  name = models.CharField(max_length=200, verbose_name='اسم العقار')
  type = models.CharField(max_length=50, choices=PROERTY_TYPES, verbose_name='نوع العقار')
  category = models.CharField(max_length=50, choices=PROPERTY_CATEGORIES, verbose_name='الفئة')
  city = models.CharField(max_length=100, verbose_name='المدينة')
  address = models.CharField(max_length=300, verbose_name='العنوان')
  description = models.TextField(blank=True, null=True, verbose_name='الوصف')
  status = models.CharField(max_length=10, choices=OCCUPANCY_STATUS, default='شاغر', verbose_name='الحالة')

  latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name='خط العرض')
  longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name='خط الطول')

  has_parking = models.BooleanField(default=False, verbose_name='يوجد موقف')
  has_elevator = models.BooleanField(default=False, verbose_name='يوجد مصعد')
  
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

class PropertyImage(models.Model):
  property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE, verbose_name='العقار')
  image = models.ImageField(upload_to='properties/images/', verbose_name='صورة')
  caption = models.CharField(max_length=100, blank=True, null=True, verbose_name='تعليق')

  def __str__(self):
    return f"صورة - {self.property.name}"