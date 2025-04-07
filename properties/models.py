from django.db import models

PROERTY_TYPES = [
  ('سكني', 'سكني'),
  ('تجاري', 'تجاري'),
  ('سكني تجاري', 'سكني تجاري'),
]
PROPERTY_CATEGORIES = [
  ('عمارة', 'عمارة'),
  ('برج', 'برج'),
  ('مركز تجاري', 'مركز تجاري'),
  ('فيلا', 'فيلا'),
  ('سكن موظفين', 'سكن موظفين'),
  ('محلات', 'محلات'),
  ('مخزن', 'مخزن'),
  ('مكتب', 'مكتب')
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

  has_parking = models.BooleanField(default=False, verbose_name='يوجد موقف')
  has_elevator = models.BooleanField(default=False, verbose_name='يوجد مصعد')

  floor_count = models.PositiveIntegerField(default=1, verbose_name='عدد الطوابق')
  unit_count = models.PositiveIntegerField(default=1, verbose_name='عدد الوحدات')
  
  latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name='خط العرض')
  longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name='خط الطول')

  is_active = models.BooleanField(default=True, verbose_name='نشط؟')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرى تعديل')

  class Meta:
    verbose_name = 'عقار'
    verbose_name_plural = 'العقارات'
    ordering = ['-created_at']

  def __str__(self):
    return self.name

class PropertyImage(models.Model):
  property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE, verbose_name='العقار')
  image = models.ImageField(upload_to='properties/images/', verbose_name='صورة')
  caption = models.CharField(max_length=100, blank=True, null=True, verbose_name='تعليق')

  class Meta:
    verbose_name = 'صورة عقار'
    verbose_name_plural = 'صور العقارات'

  def __str__(self):
    return f"صورة - {self.property.name}"