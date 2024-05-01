from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("contract/detail/<int:pk>/", views.ContractDetailView.as_view(), name="contract_detail"),
    path("contract/create/", views.CreateContractView.as_view(), name="contract_create"),
]
