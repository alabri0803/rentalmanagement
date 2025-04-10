from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class UserRole(models.TextChoices):
  OWNER = 'OWNER', _('مالك')
  INVESTOR = 'INVESTOR', _('مستثمر')
  STAFF = 'STAFF', _('موظف')

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.STAFF, verbose_name=_("الدور"))
  phone = models.CharField(
    max_length=20, 
    blank=True, 
    null=True, 
    validators=[RegexValidator(regex=r'^\+?\d{7,15}$')], 
    verbose_name=_("رقم الهاتف")
  )
  address = models.TextField(blank=True, null=True, verbose_name=_("العنوان"))
  company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("اسم المؤسسة / الشركة"))
  avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name=_("الصورة الشخصية"))
  is_verified = models.BooleanField(default=False, verbose_name=_("تم التحقق"))
  language = models.CharField(max_length=5, choices=[('ar', 'العربية'), ('en', 'English')], default='ar', verbose_name=_("اللغة"))
  last_seen = models.DateTimeField(auto_now=True, verbose_name=_("آخر نشاط"))
  created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإنشاء"))

  class Meta:
    verbose_name = _("ملف مستخدم")
    verbose_name_plural = _("ملفات المستخدمين")

  def __str__(self):
    return f"{self.user.username} ({self.get_role_display()})"

  def is_owner(self):
    return self.role == UserRole.OWNER

  def is_investor(self):
    return self.role == UserRole.INVESTOR

  def is_staff(self):
    return self.role == UserRole.STAFF

  def full_name(self):
    return f"{self.user.first_name} {self.user.last_name}".strip()