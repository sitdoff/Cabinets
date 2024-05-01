from django.urls import path

from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path("<int:user_id>/", views.profile, name="profile_view"),
    path("customer/", views.customer_office, name="customer_office"),
    path("performer/", views.performer_office, name="performer_office"),
]
