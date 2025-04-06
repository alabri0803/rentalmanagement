from django.shortcuts import get_object_or_404, render

from .models import Tenant


def tenant_list(request):
  tenants = Tenant.objects.filter(is_active=True)
  return render(request, 'tenants/list.html', {'tenants': tenants})

def tenant_detail(request, pk):
  tenant = get_object_or_404(Tenant, pk=pk)
  return render(request, 'tenants/detail.html', {'tenant': tenant})
