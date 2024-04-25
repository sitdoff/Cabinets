from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import ContractModel

# Create your views here.


class Index(ListView):
    queryset = ContractModel.objects.all()
    template_name = "index.html"
    context_object_name = "contract_list"


class ContractDetailView(DetailView):
    model = ContractModel
    template_name = "contracts/contract_detail.html"
    context_object_name = "contract"
