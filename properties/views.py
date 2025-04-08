from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import (
  DetailView,
  ListView,
)

from .forms import PropertyForm, UnitFeatureFormSet, UnitForm, UnitImageFormSet
from .models import Property


class PropertyListView(ListView):
  model = Property
  template_name = 'properties/property_list.html'
  context_object_name = 'properties'
  paginate_by = 10

  def get_queryset(self):
    return Property.objects.all().order_by('-created_at')

class PropertyCreateView(View):
  def get(self, request):
    form = PropertyForm()
    return render(request, 'properties/property_form.html', {'form': form, 'title': _('إضافة عقار جديد'),})

  def post(self, request):
    form = PropertyForm(request.POST, request.FILES)
    if form.is_valid():
      prop = form.save(commit=False)
      prop.owner = request.user
      prop.save()
      messages.success(request, _('تم إنشاء العقار بنجاح.'))
      return redirect('properties:property_detail', pk=prop.pk)
    return render(request, 'properties/property_form.html', {'form': form, 'title': _('إضافة عقار جديد'),})
    
class PropertyDetailView(DetailView):
  model = Property
  template_name = 'properties/property_detail.html'
  context_object_name = 'property'

class UnitCreateView(View):
  def get(self, request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    unit_form = UnitForm(initial={'property': property_obj})
    image_formset = UnitImageFormSet()
    feature_formset = UnitFeatureFormSet()
    return render(request, 'properties/unit_form.html',{
      'unit_form': unit_form,
      'image_formset': image_formset,
      'feature_formset': feature_formset,
      'title': _('إضافة وحدة للعقار: ') + property_obj.name,
    })

  def post(self, request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    unit_form = UnitForm(request.POST)
    image_formset = UnitImageFormSet(request.POST, request.FILES)
    feature_formset = UnitFeatureFormSet(request.POST)
    if unit_form.is_valid() and image_formset.is_valid() and feature_formset.is_valid():
      unit = unit_form.save(commit=False)
      unit.property = property_obj
      unit.save()
      image_formset.instance = unit
      image_formset.save()
      feature_formset.instance = unit
      feature_formset.save()
      messages.success(request, _('تم إنشاء الوحدة بنجاح.'))
      return redirect('properties:property_detail', pk=property_obj.pk)
    return render(request, 'properties/unit_form.html', {
      'form': unit_form,
      'image_formset': image_formset,
      'feature_formset': feature_formset,
      'property': property_obj,
      'title': _('إضافة وحدة: '),
    })