from django.db import models
from users.services import profile_user_path


# Create your models here.
class UserProfileModel(models.Model):
    """
    User profile model.
    """

    name = models.CharField(verbose_name="Name", max_length=100, blank=True)
    information = models.TextField(verbose_name="Information", blank=True)
    photo = models.ImageField(verbose_name="Profile image", upload_to=profile_user_path, blank=True)
    phone = models.CharField(verbose_name="Phone number", max_length=12, blank=True)
    user = models.OneToOneField(
        "users.UserModel", on_delete=models.CASCADE, related_name="profile", verbose_name="Profile"
    )
    # customer_profile
    # performer_profile
    # reviews =


# class CustomerProfileModel(models.Model):
#     pass
# количество размещенных заказов
# сумма размещенных заказов
# количество активных заказов


# class PerformerProfileModel(models.Model):
#     pass
# количество выполненных заказов
# сумма выполненных заказов
# количество заказов в работе
