from django.db import models

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
  unit = models.OneToOneField(Unit, on_delete=models.CASCADE, verbose_name='الوحدة', related_name='tenant')
  id_number = models.CharField(max_length=20, verbose_name='رقم الهوية/السجل التجاري')
  phone = models.CharField(max_length=15, verbose_name='رقم الهاتف')
  email = models.EmailField(blank=True, null=True, verbose_name='البريد الإلكتروني')
  contract_start = models.DateField(verbose_name='بداية العقد')
  contract_end = models.DateField(verbose_name='نهاية العقد')
  status = models.CharField(max_length=10, choices=CONTRACT_STATUS, verbose_name='حالة العقد', default='ساري')
  notes = models.TextField(blank=True, null=True, verbose_name='ملاحظات')

  class Meta:
    verbose_name = 'مستأجر'
    verbose_name_plural = 'المستأجرين'

  def __str__(self):
    return self.full_name