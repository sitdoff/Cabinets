from django.contrib import admin

from .models import UserProfileModel


# Register your models here.
@admin.register(UserProfileModel)
class UserProfileModelAdmin(admin.ModelAdmin):
    exclude = ("user",)
