from django.urls import path

from .views import cretae_offer

urlpatterns = [
    path("create/<int:contract_id>/", cretae_offer, name="offer_create"),
]
