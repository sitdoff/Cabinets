from django.contrib import admin

from .models import OfferModel


# Register your models here.
class OfferModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(OfferModel, OfferModelAdmin)
