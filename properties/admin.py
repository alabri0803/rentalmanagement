from django.contrib import admin

from .models import Feature, Property, Unit, UnitImage


class UnitImageInline(admin.TabularInline):
    model = UnitImage
    extra = 1

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1

class UnitInline(admin.TabularInline):
    model = Unit
    extra = 0
    show_change_link = True

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'owner')
    list_filter = ('city',)
    search_fields = ('name', 'address', 'owner__username')
    inlines = [UnitInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'city', 'address', 'owner', 'description')
        }),
        ('الموقع الجغرافي', {
            'fields': ('latitude', 'longitude'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'property', 'unit_type', 'floor', 'status', 'price_monthly')
    list_filter = ('unit_type', 'status', 'property__city')
    search_fields = ('name', 'property__name')
    inlines = [UnitImageInline, FeatureInline]

@admin.register(UnitImage)
class UnitImageAdmin(admin.ModelAdmin):
    list_display = ('unit', 'image')
    

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('unit', 'feature')