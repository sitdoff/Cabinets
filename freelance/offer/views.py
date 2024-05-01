from contracts.models import ContractModel
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import CreateOfferForm
from .models import OfferModel


# Create your views here.
def cretae_offer(request: HttpRequest, contract_id: int) -> HttpResponse:
    """
    Create offer view
    """
    if request.method == "POST":
        form = CreateOfferForm(request.POST)
        contract = get_object_or_404(ContractModel, pk=contract_id)
        form.instance.contract = contract
        form.instance.offering = request.user
        if form.is_valid():
            form.save()
            redirect_url = reverse("contract_detail", kwargs={"pk": contract_id})
            return redirect(redirect_url)
    else:
        form = CreateOfferForm()
    return render(request, "offer/offer_create.html", {"form": form})
