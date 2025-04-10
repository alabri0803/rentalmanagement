from django.contrib import admin
from django.utils.html import format_html

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_link', 'role', 'phone', 'is_verified', 'last_seen_display', 'language')
    list_filter = ('role', 'is_verified', 'language')
    search_fields = ('user__username', 'phone', 'company_name')
    readonly_fields = ('last_seen', 'user_avatar')
    fieldsets = (
        ("المستخدم", {"fields": ("user", "role", "is_verified")}),
        ("معلومات التواصل", {"fields": ("phone", "address", "language")}),
        ("الملف التجاري (للمستثمرين)", {"fields": ("company_name",)}),
        ("الصورة والنشاط", {"fields": ("avatar", "user_avatar", "last_seen")}),
    )
    def user_link(self, obj):
        return format_html(f'<a href="/admin/auth/user/{obj.user.id}/change/">{obj.user.username}</a>')
    user_link.short_description = "المستخدم"

    def last_seen_display(self, obj):
        return obj.last_seen.strftime("%Y-%m-%d %H:%M")
    last_seen_display.short_description = "آخر ظهور"

    def user_avatar(self, obj):
      if obj.avatar:
        return format_html(f'<img src="{obj.avatar.url}" width="60" style="border-radius: 50%;" />')
      return "-"
    user_avatar.short_description = "معاينة الصورة"

    actions = ['make_verified', 'make_unverified']

    def make_verified(self, request, queryset):
        queryset.update(is_verified=True)
        self.message_user(request, "تم تفعيل الحسابات المحددة بنجاح.")
    make_verified.short_description = "تفعيل الحسابات المحددة"

    def make_unverified(self, request, queryset):
        queryset.update(is_verified=False)
        self.message_user(request, "تم إلغاء تفعيل الحسابات المحددة بنجاح.")
    make_unverified.short_description = "إلغاء تفعيل الحسابات المحددة"