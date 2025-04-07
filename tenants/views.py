from django.urls import reverse_lazy
from django.views.generic import (
  CreateView,
  DeleteView,
  DetailView,
  ListView,
  UpdateView,
)

from .forms import TenantForm
from .models import Tenant


class TenantListView(ListView):
  model = Tenant
  template_name = 'tenants/tenant_list.html'
  context_object_name = 'tenants'


class TenantDetailView(DetailView):
  model = Tenant
  template_name = 'tenants/tenant_detail.html'

class TenantCreateView(CreateView):
  model = Tenant
  form_class = TenantForm
  template_name = 'tenants/tenant_form.html'
  success_url = reverse_lazy('tenants:tenant_list')

class TenantUpdateView(UpdateView):
  model = Tenant
  form_class = TenantForm
  template_name = 'tenants/tenant_form.html'
  success_url = reverse_lazy('tenants:tenant_list')

class TenantDeleteView(DeleteView):
  model = Tenant
  template_name = 'tenants/tenant_confirm_delete.html'
  success_url = reverse_lazy('tenants:tenant_list')