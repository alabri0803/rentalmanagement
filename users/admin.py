from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone')
    search_fields = ('user__username', 'phone')
    list_filter = ('user__username', 'phone',)