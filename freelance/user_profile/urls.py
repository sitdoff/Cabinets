from django.urls import path

from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path("customer/", views.customer_office, name="customer_office"),
]
