from django.db import models


class Property(models.Model):
  PROERTY_TYPES = [
    ('apartment', 'شقة'),
    ('office', 'مكتب'),
    ('shop', 'محل'),
    ('warehouse', 'مخزن'),
    ('parking', 'موقف')
  ]
  name = models.CharField(max_length=255)
  property_type = models.CharField(max_length=50, choices=PROERTY_TYPES)
  owner_share = models.DecimalField(max_digits=5, decimal_places=2, help_text='نسبة المالك')
  investor_share = models.DecimalField(max_digits=5, decimal_places=2, help_text='نسبة المستثمر')
  rent_price = models.DecimalField(max_digits=10, decimal_places=2)
  is_available = models.BooleanField(default=True)

  def __str__(self):
    return f"{self.name} - {self.get_property_type_display()}"