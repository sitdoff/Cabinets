from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
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
    use_in_migrations = True

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        if username is None and not email is None:
            username = email
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        if username is None and not email is None:
            username = email
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class UserModel(AbstractUser):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        verbose_name="username",
        max_length=150,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
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
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            UserProfile.objects.create(user=self)


class UserProfile(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100, blank=True)
    information = models.TextField(verbose_name="Information", blank=True)
    photo = models.ImageField(verbose_name="Profile image", upload_to=profile_user_path, blank=True)
    phone = models.CharField(verbose_name="Phone number", max_length=12, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile", verbose_name="Profile")
    # customer_profile
    # performer_profile
    # reviews =
