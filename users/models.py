from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRole(models.TextChoices):
  OWNER = 'OWNER', _('مالك')
  INVESTOR = 'INVESTOR', _('مستثمر')
  STAFF = 'STAFF', _('موظف')

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.STAFF)
  phone = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("رقم الهاتف"))
  address = models.TextField(blank=True, null=True, verbose_name=_("العنوان"))

  def __str__(self):
    return f"{self.user.username} ({self.get_role_display()})"