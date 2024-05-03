from django.test import TestCase
from django.urls import reverse
from users.models import UserModel

from .models import CategoryModel, ContractModel


class TestContractCreateView(TestCase):
    """
    Test contract create view
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.category1 = CategoryModel.objects.create(name="test_category1")
        cls.user1 = UserModel.objects.create_user(email="user1@mail.com", password="password")
        return super().setUpClass()

    def setUp(self) -> None:
        return super().setUp()

    def test_customer(self):
        """
        Testing the installation of the current user as a customer when creating a contract.
        """
        contract_data = {
            "title": "test_contract1_title",
            "information": "test_contract1_information",
            "value": 10.5,
            "category": self.category1.pk,
        }
        self.client.force_login(self.user1)
        response = self.client.post(reverse("contract_create"), data=contract_data)
        self.assertEqual(response.status_code, 302)

        contract = ContractModel.objects.get(title=contract_data["title"])
        self.assertIsNone(contract.performer)
        self.assertIsNotNone(contract.customer)
        self.assertEqual(contract.customer, self.user1)
