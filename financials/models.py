from django.db import models

from properties.models import Property
from tenants.models import Tenant


class Income(models.Model):
  tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True, verbose_name='المستأجر')
  property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, verbose_name='العقار')
  amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='المبلغ')
  date = models.DateField(verbose_name='التاريخ الدخل')
  description = models.TextField(max_length=255, verbose_name='الوصف')

  def __str__(self):
    return f"دخل: {self.amount} - {self.date}"

class Expense(models.Model):
  property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, verbose_name='العقار')
  amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='المبلغ')
  date = models.DateField(verbose_name='تاريخ المصروف')
  description = models.TextField(max_length=255, verbose_name='الوصف')

  def __str__(self):
    return f"مصروف: {self.amount} - {self.description}"

class DistributionSetting(models.Model):
  owner_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=50.00, verbose_name='نسبة المالك')
  investor_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=50.00, verbose_name='نسبة المستثمر')

  def __str__(self):
    return f"توزيع: مالك {self.owner_percentage}% /  مستثمر {self.investor_percentage}%"