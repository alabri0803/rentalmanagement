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
  company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("اسم المؤسسة / الشركة"))
  avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name=_("الصورة الشخصية"))
  is_verified = models.BooleanField(default=False, verbose_name=_("تم التحقق"))
  language = models.CharField(max_length=10, choices=[('ar', 'العربية'), ('en', 'English')], default='ar')
  last_seen = models.DateTimeField(auto_now=True, verbose_name=_("آخر نشاط"))

  def __str__(self):
    return f"{self.user.username} ({self.get_role_display()})"

  def is_owner(self):
    return self.role == UserRole.OWNER

  def is_investor(self):
    return self.role == UserRole.INVESTOR

  def is_staff(self):
    return self.role == UserRole.STAFF