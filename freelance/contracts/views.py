from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import ContractCreateModelForm
from .models import ContractModel


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

    def get_queryset(self):
        """
        Join customer to profile object
        """
        queryset = super().get_queryset().select_related("customer")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["is_offered"] = (
                context[self.context_object_name].contract_offers.filter(offering=self.request.user).exists()
            )
        return context


class CreateContractView(LoginRequiredMixin, CreateView):
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
