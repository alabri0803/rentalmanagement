from django.db import models
from django.utils import timezone

from properties.models import Unit


class Tenant(models.Model):
  TENANT_TYPE_CHOICES = [
    ('فرد', 'فرد'),
    ('شركة', 'شركة')
  ]
  CONTRACT_STATUS = [
    ('ساري', 'ساري'),
    ('منتهي', 'منتهي'),
    ('ملغي', 'ملغي')
  ]
  full_name = models.CharField(max_length=100, verbose_name='الاسم الكامل')
  tenant_type = models.CharField(max_length=10, choices=TENANT_TYPE_CHOICES, verbose_name='نوع المستأجر')
  unit = models.OneToOneField(Unit, on_delete=models.CASCADE, related_name='tenant', verbose_name='الوحدة')
  id_number = models.CharField(max_length=20, verbose_name='رقم الهوية/السجل التجاري')
  phone = models.CharField(max_length=15, verbose_name='رقم الهاتف')
  email = models.EmailField(blank=True, null=True, verbose_name='البريد الإلكتروني')
  contract_start = models.DateField(verbose_name='تاريخ بداية العقد')
  contract_end = models.DateField(verbose_name='تاريخ نهاية العقد')
  status = models.CharField(max_length=10, choices=CONTRACT_STATUS, default='ساري', verbose_name='حالة العقد')

  id_document = models.ImageField(upload_to='tenants/id_docs/', blank=True, null=True, verbose_name='صورة البطاقة')
  contract_file = models.FileField(upload_to='tenants/contracts/', blank=True, null=True, verbose_name='نسخة من عقد الإيجار')
  
  notes = models.TextField(blank=True, null=True, verbose_name='ملاحظات إضافية')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

  class Meta:
    verbose_name = 'مستأجر'
    verbose_name_plural = 'المستأجرين'
    ordering = ['-created_at']

  def __str__(self):
    return self.full_name

  @property
  def days_remaining(self):
    if self.contract_end and self.contract_end > timezone.now().date():
      return (self.contract_end - timezone.now().date()).days
    return 0

  @property
  def is_expired(self):
    return self.contract_end and self.contract_end < timezone.now().date()

  @property
  def contract_duration(self):
    if self.contract_start and self.contract_end:
      return (self.contract_end - self.contract_start).days
    return None