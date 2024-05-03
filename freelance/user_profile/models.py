from datetime import datetime

from contracts.models import ContractModel
from django.db import models
from django.db.models import Sum
from offer.models import OfferModel
from PIL import Image
from users.services import profile_user_path


class UserProfileModel(models.Model):
    """
    User profile model.
    """

    name = models.CharField(verbose_name="Name", max_length=100, blank=True)
    information = models.TextField(verbose_name="Information", blank=True)
    photo = models.ImageField(
        verbose_name="Profile image",
        upload_to=profile_user_path,
        blank=True,
    )
    contact = models.TextField(verbose_name="Ваши данные для связи", max_length=500, blank=True)
    user = models.OneToOneField(
        "users.UserModel", on_delete=models.CASCADE, related_name="profile", verbose_name="User"
    )

    def __str__(self) -> str:
        return f"{self.user} profile"

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            img.resize((350, 350))
            img.save(self.photo.path)

    def get_categories_performed(self):
        """
        Returns the categories in which the user completed contracts.
        """
        return (
            self.user.completed_contracts.filter(completed=True)
            .values_list("category__pk", "category__name")
            .annotate(performed_contracts=models.Count("category__contracts__performer" == self.user))
            .distinct()
        )

    def get_categories_created(self):
        """
        Returns the categories in which the user created contracts.
        """
        return (
            self.user.placed_contracts.all()
            .values_list("category__pk", "category__name")
            .annotate(performed_contracts=models.Count("category__contracts__customer" == self.user))
            .distinct()
        )

    def get_placed_contracts(self):
        """
        Returns the created contracts.
        """
        return self.user.placed_contracts.filter(completed=False)


class CustomerProfileModel(UserProfileModel):
    """
    Contract creator profile model.

    Proxy model.
    """

    class Meta:
        proxy = True

    def get_offers(self):
        """
        Returns offers for all outstanding contracts.
        """
        offers = (
            OfferModel.objects.select_related("offering", "offering__profile")
            .prefetch_related("contract")
            .filter(contract__customer=self.user)
            .order_by("-created_at")
        )
        return offers

    def get_placed_contracts(self):
        queryset = super().get_placed_contracts().filter(completed=False).order_by("created_at")
        return queryset

    def get_amount_for_month(self):
        current_month = datetime.now().month
        current_year = datetime.now().year

        total_value = ContractModel.objects.filter(
            created_at__month=current_month,
            created_at__year=current_year,
            customer=self.user,
        ).aggregate(total=Sum("value"))["total"]
        if total_value is None:
            total_value = 0

        return total_value


class PerformerProfileModel(UserProfileModel):
    """
    Contract performer profile model.

    Proxy model.
    """

    class Meta:
        proxy = True

    def get_offers(self):
        """
        Returns all offers submitted by the user
        """
        offers = (
            OfferModel.objects.select_related("offering")
            .prefetch_related("contract", "contract__customer")
            .filter(offering=self.user)
        )
        return offers

    def get_completed_contracts(self):
        queryset = ContractModel.objects.select_related("category").filter(performer=self.user).filter(completed=True)
        return queryset

    def get_uncompleted_contracts(self):
        queryset = ContractModel.objects.select_related("category").filter(performer=self.user, completed=False)
        return queryset

    def get_amount_for_month(self):
        current_month = datetime.now().month
        current_year = datetime.now().year

        total_value = ContractModel.objects.filter(
            updated_at__month=current_month,
            updated_at__year=current_year,
            completed=True,
            performer=self.user,
        ).aggregate(total=Sum("value"))["total"]
        if total_value is None:
            total_value = 0

        return total_value
