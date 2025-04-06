from django.shortcuts import get_object_or_404, render

from .models import Property


def property_list(request):
  properties = Property.objects.filter(is_available=True)
  return render(request, 'properties/list.html', {'properties': properties})

def property_detail(request, pk):
  property = get_object_or_404(Property, pk=pk)
  return render(request, 'properties/detail.html', {'property': property})