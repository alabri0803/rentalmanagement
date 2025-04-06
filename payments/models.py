from django.db import models

from properties.models import Property
from tenants.models import Tenant


class Payment(models.Model):
  tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name='المستأجر')
  property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='العقار')
  amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='المبلغ المدفوع')
  payment_date = models.DateField(verbose_name='تاريخ الدفع')
  period_start = models.DateField(verbose_name='بداية الفترة')
  period_end = models.DateField(verbose_name='نهاية الفترة')
  is_late = models.BooleanField(default=False, verbose_name='متأخر؟')
  notes = models.TextField(blank=True, null=True, verbose_name='ملاحظات')

  def __str__(self):
    return f"{self.tenant} | {self.amount} لـــ ر.ع {self.period_start:%Y-%m}"