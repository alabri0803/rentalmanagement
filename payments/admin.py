from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
  list_display = ('tenant', 'property', 'amount', 'payment_date', 'is_late')
  list_filter = ('is_late', 'payment_date')
  search_fields = ('tenant__user__username', 'property__name')