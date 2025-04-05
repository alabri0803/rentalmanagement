from django.contrib.auth.models import User
from django.db import models

from properties.models import Property


class Tenant(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  commercial_license = models.CharField(max_length=50, blank=True, null=True, help_text='السجل التجاري')
  rent_property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, related_name='tenants')
  lease_start_date = models.DateField()
  lease_end_date = models.DateField()
  monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.user.username