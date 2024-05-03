from django.contrib import admin

from .models import UserProfileModel


@admin.register(UserProfileModel)
class UserProfileModelAdmin(admin.ModelAdmin):
    exclude = ("user",)
