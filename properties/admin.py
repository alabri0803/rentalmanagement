from django.contrib import admin

from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'property_type', 'rent_price', 'is_available')
    list_filter = ('property_type', 'is_available')
    search_fields = ('name',)