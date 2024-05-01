from contracts.models import ContractModel
from django.db import models
from users.models import UserModel


# Create your models here.
class OfferModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    offering = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="user_offers")
    contract = models.ForeignKey(ContractModel, on_delete=models.CASCADE, related_name="contract_offers")
    message = models.TextField(max_length=500, blank=True, verbose_name="Сопроводительное письмо")

    class Meta:
        verbose_name_plural = "Offers"

    def __str__(self) -> str:
        return f"{self.offering} offer {self.contract}"
