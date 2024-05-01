from django.forms import ModelForm, forms

from .models import OfferModel


class CreateOfferForm(ModelForm):
    class Meta:
        model = OfferModel
        fields = ("message",)
