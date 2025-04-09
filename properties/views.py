from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Unit
from .forms import PropertyForm, UnitForm, UnitImageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})

@login_required
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property_detail.html', {'property': property})

@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تمت إضافة العقار بنجاح.')
            return redirect('properties:property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/property_form.html', {'form': form})

@login_required
def add_unit(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        unit_form = UnitForm(request.POST)
        if unit_form.is_valid():
            unit = unit_form.save(commit=False)
            unit.property = property
            unit.save()
            messages.success(request, 'تمت إضافة الوحدة بنجاح.')
            return redirect('properties:property_detail', pk=property.id)
    else:
        form = UnitForm(initial={'property': property})
    return render(request, 'properties/unit_form.html', {'form': form, 'property': property})