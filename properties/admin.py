from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import Property, PropertyCategory, Unit, UnitFeature, UnitImage


class UnitImageInline(admin.TabularInline):
    model = UnitImage
    extra = 1
    fields = ['image', 'preview', 'caption']
    readonly_fields = ['preview',]

    def preview(self, obj):
      if obj.image:
        return format_html('<img src="{}" width= "100" style="border:1px solid #ccc;" />', obj.image.url)
      return "-"
    preview.short_description = "معاينة"

class UnitFeatureInline(admin.TabularInline):
    model = UnitFeature
    extra = 1

class UnitInline(admin.TabularInline):
    model = Unit
    extra = 1
    show_change_link = True

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'governorate', 'category', 'total_units', 'created_at', 'owner')
    list_filter = ('city', 'governorate', 'category')
    search_fields = ('name', 'address', 'city', 'governorate')
    inlines = [UnitInline]
    fieldsets = (
        (_('معلومات العقار'), {
            'fields': ('name', 'description', 'image')
        }),
        (_('الموقع'), {
            'fields': ('address', 'city', 'governorate')
        }),
        (_('تنصيف وإدارة العقار'), {
            'fields': ('category', 'total_units', 'owner')
        })
    )

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'property', 'unit_type', 'status', 'price_monthly', 'floor', 'area_sqm')
    list_filter = ('status', 'unit_type', 'property__city')
    search_fields = ('name', 'property__name')
    inlines = [UnitImageInline, UnitFeatureInline]
    list_editable = ('status', 'price_monthly')
    fieldsets = (
        (_('تفاصيل الوحدة'), {
            'fields': ('property', 'name', 'unit_type', 'floor', 'area_sqm')
        }),
        (_('الإيجار والحالة'), {
            'fields': ('price_monthly', 'status', 'notes')
        }),
    )

@admin.register(PropertyCategory)
class PropertyCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(UnitImage)
class UnitImageAdmin(admin.ModelAdmin):
    list_display = ('unit', 'caption', 'thumbnail')
    readonly_fields = ('thumbnail',)

    def thumbnail(self, obj):
      if obj.image:
        return format_html('<img src="{}" width="80" style="border:1px solid #ddd;" />', obj.image.url)
      return "-"
    thumbnail.short_description = "صورة"

@admin.register(UnitFeature)
class UnitFeatureAdmin(admin.ModelAdmin):
    list_display = ('unit', 'feature_name')
    search_fields = ('feature_name',)