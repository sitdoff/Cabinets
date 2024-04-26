from django.conf import settings


def profile_user_path(instance: "UserModel", filename: str | None = None) -> str:
    """
    Returns the path to the user profile folder for storing images
    """
    return f"profile_pictures/{instance.user.pk}/{filename}"
