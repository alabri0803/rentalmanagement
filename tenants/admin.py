from django.contrib import admin

from .models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
  list_display = ('user', 'rent_property', 'lease_start_date', 'lease_end_date', 'is_active')
  list_filter = ('is_active',)
  search_fields = ('user__username', 'national_id', 'commercial_license')