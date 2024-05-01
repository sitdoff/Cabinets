from django.contrib import admin

from .models import CategoryModel, ContractModel


# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
    pass


class ContractModelAdmin(admin.ModelAdmin):
    list_display = ["title", "value", "customer", "performer", "completed"]


admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(ContractModel, ContractModelAdmin)
