from django.test import TestCase

from .models import UserModel, UserProfile
from .services import profile_user_path


# Create your tests here.
class TestFunctionProfileUserPath(TestCase):
    """
    Test a function that returns the path to where the user's files are stored.
    """

    def test_profile_user_path(self):
        data = {
            "email": "user@mail.com",
            "password": "password",
        }
        user = UserModel.objects.create_user(**data)
        result = profile_user_path(user)
        self.assertEqual(result, f"profile/{user.username}/")


class TestUserModel(TestCase):
    """
    Test the user model.
    """

    def test_create_user_with_username(self):
        """
        Test user creation using username.
        """
        data = {
            "username": "user",
            "email": "user@mail.com",
            "password": "password",
        }
        user = UserModel.objects.create_user(**data)
        self.assertEqual(user.username, data["username"])
        self.assertEqual(user.email, data["email"])
        self.assertTrue(user.check_password(data["password"]))

    def test_create_user_without_username(self):
        """
        Test user creation without using a username.
        """
        data = {
            "email": "user@mail.com",
            "password": "password",
        }
        user = UserModel.objects.create_user(**data)
        self.assertEqual(user.username, data["email"])
        self.assertEqual(user.email, data["email"])
        self.assertTrue(user.check_password(data["password"]))

    def test_create_profile(self):
        """
        Test the creation of a user profile when creating a user.
        """
        data = {
            "email": "user@mail.com",
            "password": "password",
        }
        user = UserModel.objects.create_user(**data)
        self.assertIsInstance(user.profile, UserProfile)
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(user.profile, profile)
        self.assertEqual(profile.user, user)


class TestEmailUsernameAuthenticationBackend(TestCase):
    """
    Test a authentication backend.
    """

    @classmethod
    def setUpTestData(cls) -> None:
        cls.data = {
            "email": "user@mail.com",
            "password": "password",
        }
        cls.user = UserModel.objects.create_user(**cls.data)
        return super().setUpTestData()

    def test_login_with_email(self):
        """
        Test authentication using email.
        """
        from django.contrib.auth import authenticate

        user = authenticate(email=self.data["email"], password=self.data["password"])
        self.assertIsNotNone(user)
