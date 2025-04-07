from django.contrib import admin
from django.utils import timezone

from .models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'tenant_type', 'unit', 'phone', 'contract_start', 'contract_end', 'status', 'days_remaining_display')
  list_filter = ('status', 'tenant_type', 'contract_end')
  search_fields = ('full_name', 'id_number', 'phone', 'unit__name')
  date_hierarchy = 'contract_end'
  readonly_fields = ('created_at', 'updated_at', 'days_remaining_display')
  fieldsets = (
    ('بيانات المستأجر', {
      'fields': ('full_name', 'tenant_type', 'unit', 'id_number', 'phone', 'email')
    }),
    ('تفاصيل العقد', {
      'fields': ('contract_start', 'contract_end', 'status', 'contract_file')
    }),
    ('الوثائق', {
      'fields': ('id_document',)
    }),
    ('ملاحظات وبيانات إضافية', {
      'fields': ('notes', 'created_at', 'updated_at', 'days_remaining_display')
    }),
  )
  def days_remaining_display(self, obj):
    if obj.is_expired:
      return f"منتهي منذ {(timezone.now().date() - obj.contract_end).days} يوم"
    return f"{obj.days_remaining} يوم متبقي"
  days_remaining_display.short_description = 'عدد الايام المتبقية'