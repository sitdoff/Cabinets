from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserModel


class UserRegisterationForm(UserCreationForm):
    """
    Form for a user creation
    """

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="",
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = UserModel
        fields = ("email", "password1", "password2")
