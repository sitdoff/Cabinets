from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from user_profile.models import UserProfileModel


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

    profile: "UserProfileModel"

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
            UserProfileModel.objects.create(user=self)
