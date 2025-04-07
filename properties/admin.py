from django.contrib import admin

from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'city', 'num_apartments', 'num_shops')
    search_fields = ('name', 'city')
    list_filter = ('city', 'type')