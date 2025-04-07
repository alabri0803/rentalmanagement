from django.shortcuts import get_object_or_404, redirect, render

from .forms import PropertyForm
from .models import Property


def property_list(request):
  query = request.GET.get('q', '')
  properties = Property.objects.filter(name__icontains=query) if query else Property.objects.all()
  return render(request, 'properties/list.html', {'properties': properties, 'query': query})
  
def property_detail(request, pk):
  property = get_object_or_404(Property, pk=pk)
  return render(request, 'properties/detail.html', {'property': property})

def property_create(request):
  if request.method == 'POST':
    form = PropertyForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('property_list')
  else:
    form = PropertyForm()
  return render(request, 'properties/form.html', {'form': form})