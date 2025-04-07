from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
  CreateView,
  DeleteView,
  DetailView,
  ListView,
  UpdateView,
)

from .forms import PropertyForm, PropertyImageUploadForm, UnitForm
from .models import Property, Unit


class PropertyListView(ListView):
  model = Property
  template_name = 'properties/property_list.html'
  context_object_name = 'properties'
  paginate_by = 10

  def get_queryset(self):
    return Property.objects.filter(is_active=True)

class PropertyDetailView(DetailView):
  model = Property
  template_name = 'properties/property_detail.html'
  context_object_name = 'property'

class PropertyCreateView(CreateView):
  model = Property
  form_class = PropertyForm
  template_name = 'properties/property_form.html'
  success_url = reverse_lazy('properties:property_list')

class PropertyUpdateView(UpdateView):
  model = Property
  form_class = PropertyForm
  template_name = 'properties/property_form.html'
  success_url = reverse_lazy('properties:property_list')

class PropertyDeleteView(DeleteView):
  model = Property
  template_name = 'properties/property_confirm_delete.html'
  success_url = reverse_lazy('properties:property_list')

class PropertyImageUploadView(View):
  template_name = 'properties/property_image_upload.html'

  def get(self, request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    form = PropertyImageUploadForm()
    return render(request, self.template_name, {'form': form, 'property': property_obj})

  def post(self, request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    form = PropertyImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
      image = form.save(commit=False)
      image.property = property_obj
      image.save()
      messages.success(request, 'تم رفع الصورة بنجاح.')
      return redirect('properties:property_detail', pk=pk)
    return render(request, self.template_name, {'form': form, 'property': property_obj})

class UnitCreateView(CreateView):
  model = Unit
  form_class = UnitForm
  template_name = 'properties/unit_form.html'

  def form_valid(self, form):
    property_id = self.kwargs.get('property_id')
    form.instance.property_id = property_id
    return super().form_valid(form)

  def get_success_url(self):
    return reverse_lazy('properties:property_detail', kwargs={'pk': self.object.property.id})

class UnitUpdateView(UpdateView):
  model = Unit
  form_class = UnitForm
  template_name = 'properties/unit_form.html'

  def get_success_url(self):
    return reverse_lazy('properties:property_detail', kwargs={'pk': self.object.property.id})

class UnitDeleteView(DeleteView):
  model = Unit
  template_name = 'properties/unit_confirm_delete.html'

  def get_success_url(self):
    return reverse_lazy('properties:property_detail', kwargs={'pk': self.object.property.id})