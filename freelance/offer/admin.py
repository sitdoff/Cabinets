from django.contrib import admin

from .models import OfferModel


class OfferModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(OfferModel, OfferModelAdmin)
