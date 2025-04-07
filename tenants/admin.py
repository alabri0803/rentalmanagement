from django.contrib import admin

from .models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'tenant_type', 'unit', 'contract_start', 'contract_end')
  search_fields = ('full_name', 'id_number')
  list_filter = ('tenant_type', 'status')