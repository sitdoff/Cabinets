from django.forms import ModelForm, forms

from .models import OfferModel


class CreateOfferForm(ModelForm):
    """
    Create offer form
    """

    class Meta:
        model = OfferModel
        fields = ("message",)
