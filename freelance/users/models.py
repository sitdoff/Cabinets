from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


def profile_user_path(instance: "UserModel", filename: str) -> str:
    """
    Returns the path to the user profile folder for storing images
    """
    return f"profile/{instance.username}/"


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


class UserModelManager(UserManager):
    """
    When creating a user and superuser, the username value is replaced by email.
    """

    use_in_migrations = True

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        if username is None and not email is None:
            username = email
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        if username is None and not email is None:
            username = email
        return super().create_superuser(username, email, password, **extra_fields)


class UserModel(AbstractUser):
    """
    A user model prepared for authentication using email.
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        verbose_name="username",
        max_length=150,
        help_text="Not required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
        null=True,
        blank=True,
    )
    email = models.EmailField("email address", unique=True)

    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserModelManager()

    def save(self, *args, **kwargs):
        """
        When you create a user, a profile is created.
        """
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            UserProfile.objects.create(user=self)


class UserProfile(models.Model):
    """
    User profile model.
    """

    name = models.CharField(verbose_name="Name", max_length=100, blank=True)
    information = models.TextField(verbose_name="Information", blank=True)
    photo = models.ImageField(verbose_name="Profile image", upload_to=profile_user_path, blank=True)
    phone = models.CharField(verbose_name="Phone number", max_length=12, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile", verbose_name="Profile")
    # customer_profile
    # performer_profile
    # reviews =
