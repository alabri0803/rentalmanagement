from django.contrib import messages
from django.db.models import Q
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
  paginate_by = 20

  def get_queryset(self):
    queryset = super().get_queryset().select_related('unit')
    q = self.request.GET.get('q')
    status = self.request.GET.get('status')
    if q:
      queryset = queryset.filter(
        Q(full_name__icontains=q) |
        Q(id_number__icontains=q) |
        Q(phone__icontains=q) |
        Q(unit__name__icontains=q)
      )
    if status:
      queryset = queryset.filter(status=status)
    return queryset


class TenantDetailView(DetailView):
  model = Tenant
  template_name = 'tenants/tenant_detail.html'

class TenantCreateView(CreateView):
  model = Tenant
  form_class = TenantForm
  template_name = 'tenants/tenant_form.html'
  success_url = reverse_lazy('tenants:tenant_list')

  def form_valid(self, form):
    messages.success(self.request, 'تم إضافة المستأجر بنجاح.')
    return super().form_valid(form)

class TenantUpdateView(UpdateView):
  model = Tenant
  form_class = TenantForm
  template_name = 'tenants/tenant_form.html'
  success_url = reverse_lazy('tenants:tenant_list')

  def form_valid(self, form):
    messages.success(self.request, 'تم تحديث بيانات المستأجر بنجاح.')
    return super().form_valid(form)

class TenantDeleteView(DeleteView):
  model = Tenant
  template_name = 'tenants/tenant_confirm_delete.html'
  success_url = reverse_lazy('tenants:tenant_list')

  def delete(self, request, *args, **kwargs):
    messages.success(self.request, 'تم حذف المستأجر بنجاح.')
    return super().delete(request, *args, **kwargs)