from django.contrib import admin

from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
    verbose_name = 'صورة'
    verbose_name_plural = 'صور العقار'
    fields = ['image', 'caption']
    readonly_fields = []
    
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'category', 'city', 'status', 'is_active')
    list_filter = ('type', 'status', 'category', 'city', 'has_parking', 'has_elevator')
    search_fields = ('name', 'city', 'address')
    ordering = ('-created_at',)
    inlines = [PropertyImageInline]
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('name', 'type', 'category', 'description', 'is_active')
        }),
        ('الموقع', {
            'fields': ('city', 'address', 'latitude', 'longitude')
        }),
        ('مواصفات العقار', {
            'fields': ('status', 'floor_count', 'unit_count', 'has_parking', 'has_elevator')
        }),
        ('تواريخ', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 25

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'caption', 'image')
    search_fields = ('caption', 'property__name')
    list_filter = ('property__city',)