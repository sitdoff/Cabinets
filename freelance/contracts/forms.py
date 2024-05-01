from django.forms import ModelForm

from .models import ContractModel


class ContractCreateModelForm(ModelForm):
    class Meta:
        model = ContractModel
        fields = ["title", "information", "category", "value"]
