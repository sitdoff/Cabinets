from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import ContractCreateModelForm
from .models import ContractModel

# Create your views here.


class Index(ListView):
    """
    Main page view
    """

    queryset = ContractModel.objects.filter(performer=None, completed=False)
    template_name = "index.html"
    context_object_name = "contract_list"


class ContractDetailView(DetailView):
    """
    Contract detail view
    """

    model = ContractModel
    template_name = "contracts/contract_detail.html"
    context_object_name = "contract"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_offered"] = (
            context[self.context_object_name].contract_offers.filter(offering=self.request.user).exists()
        )
        return context


class CreateContractView(CreateView):
    """
    Create contract view
    """

    model = ContractModel
    form_class = ContractCreateModelForm
    template_name = "contracts/contract_create.html"

    def form_valid(self, form):
        """
        Set contract customer
        """
        form.instance.customer = self.request.user
        return super().form_valid(form)
