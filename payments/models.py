from django.db import models


class Payment(models.Model):
  tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE, related_name='payments')
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  payment_date = models.DateField(auto_now_add=True)
  payment_method = models.CharField(max_length=50, choices=[('bank', 'تحويل بنكي'), ('card', 'بطاقة ائتمان')])
  status = models.CharField(max_length=20, choices=[('pending', 'قيد المعالجة'), ('completed', 'مدفوع'), ('failed', 'فشل')])

  def __str__(self):
    return f"مدفوعات {self.tenant.user.username} for {self.amount} ريال"