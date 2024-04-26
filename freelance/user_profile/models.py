from django.db import models
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
        return (
            self.user.completed_contracts.all()
            .values_list("category__pk", "category__name")
            .annotate(performed_contracts=models.Count("category__contracts__performer" == self.user))
            .distinct()
        )

    def get_categories_created(self):
        return (
            self.user.placed_contracts.all()
            .values_list("category__pk", "category__name")
            .annotate(performed_contracts=models.Count("category__contracts__customer" == self.user))
            .distinct()
        )

    def get_placed_contracts(self):
        return self.user.placed_contracts.filter(completed=False)


class CustomerProfileModel(UserProfileModel):
    class Meta:
        proxy = True

    def get_contracts_created(self):
        queryset = self.user.placed_contracts.all()
        objects_pairs = zip(queryset[::2], queryset[1::2])
        return objects_pairs


# количество размещенных заказов
# сумма размещенных заказов
# количество активных заказов


# class PerformerProfileModel(models.Model):
#     pass
# количество выполненных заказов
# сумма выполненных заказов
# количество заказов в работе
