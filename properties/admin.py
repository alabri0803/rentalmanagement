from django.contrib import admin

from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
    
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'city', 'status')
    search_fields = ('name', 'city')
    list_filter = ('type', 'city', 'status', 'category')
    inlines = [PropertyImageInline]

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'caption')