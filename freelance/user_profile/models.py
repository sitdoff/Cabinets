from django.db import models
from offer.models import OfferModel
from PIL import Image
from users.services import profile_user_path


# Create your models here.
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
    phone = models.CharField(verbose_name="Phone number", max_length=12, blank=True)
    user = models.OneToOneField(
        "users.UserModel", on_delete=models.CASCADE, related_name="profile", verbose_name="User"
    )
    # customer_profile
    # performer_profile
    # reviews =

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
            self.user.completed_contracts.all()
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


# количество размещенных заказов
# сумма размещенных заказов
# количество активных заказов


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


# количество выполненных заказов
# сумма выполненных заказов
# количество заказов в работе
