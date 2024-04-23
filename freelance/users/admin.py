from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserModel


# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    pass
    search_fields = ("email", "username")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(UserModel, UserModelAdmin)
