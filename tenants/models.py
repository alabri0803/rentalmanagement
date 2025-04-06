from django.contrib.auth.models import User
from django.db import models

from properties.models import Property


class Tenant(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='المستخدم')
  national_id = models.CharField(max_length=20, verbose_name='الرقم المدني')
  commercial_license = models.CharField(max_length=100, blank=True, null=True, verbose_name='السجل التجاري')
  phone_number = models.CharField(max_length=20, verbose_name='رقم الهاتف')
  email = models.EmailField(verbose_name='البريد الإلكتروني')
  rent_property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, verbose_name='العقار المستأجر')
  lease_start_date = models.DateField(verbose_name='بداية العقد')
  lease_end_date = models.DateField(verbose_name='نهاية العقد')
  is_active = models.BooleanField(default=True, verbose_name='نشط؟')

  def __str__(self):
    return self.user.get_full_name() or self.user.username