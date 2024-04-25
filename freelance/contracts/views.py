from django.shortcuts import render
from django.views.generic import ListView

from .models import ContractModel

# Create your views here.


class Index(ListView):
    queryset = ContractModel.objects.all()
    template_name = "index.html"
    context_object_name = "contract_list"
