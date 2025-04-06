from django.shortcuts import get_object_or_404, render

from .models import Payment


def payment_list(request):
  payments = Payment.objects.all().order_by('-payment_date')
  return render(request, 'payments/list.html', {'payments': payments})

def payment_detail(request, pk):
  payment = get_object_or_404(Payment, pk=pk)
  return render(request, 'payments/detail.html', {'payment': payment})