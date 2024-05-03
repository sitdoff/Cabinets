from django.contrib import admin

from .models import UserModel


class UserModelAdmin(admin.ModelAdmin):
    search_fields = ("email", "username")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(UserModel, UserModelAdmin)
