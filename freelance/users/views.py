from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import UserRegisterationForm


# Create your views here.
def register(request: HttpRequest) -> HttpResponse:
    """
    User registration.

    After successful registration, the user is authorized using the specified data.
    """
    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(email=form.cleaned_data["email"], password=form.cleaned_data["password1"])
            login(request, user)
            return redirect("profile")
    else:
        form = UserRegisterationForm()
    return render(request, "registration/registration.html", context={"form": form})
