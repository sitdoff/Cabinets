from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from .models import CustomerProfileModel, PerformerProfileModel, UserProfileModel


@login_required
def profile(request: HttpRequest, user_id=None):
    if user_id is None:
        profile = UserProfileModel.objects.select_related().get(user=request.user.pk)
    else:
        profile = UserProfileModel.objects.select_related().get(user=user_id)
    return render(request, "profile/profile.html", context={"profile": profile})


@login_required
def customer_office(request: HttpRequest) -> HttpResponse:
    profile = CustomerProfileModel.objects.select_related().get(user=request.user.pk)
    return render(request, "profile/customer.html", context={"profile": profile})


@login_required
def performer_office(request: HttpRequest) -> HttpResponse:
    profile = PerformerProfileModel.objects.select_related().get(user=request.user.pk)
    return render(request, "profile/performer.html", context={"profile": profile})


class ProfileEdit(LoginRequiredMixin, UpdateView):
    model = UserProfileModel
    template_name = "profile/profile_edit.html"
    fields = ("name", "information", "photo", "contact")
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user.profile
