from django.db import models


class OfferModel(models.Model):
    """
    Offer model
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    offering = models.ForeignKey("users.UserModel", on_delete=models.CASCADE, related_name="user_offers")
    contract = models.ForeignKey("contracts.ContractModel", on_delete=models.CASCADE, related_name="contract_offers")
    message = models.TextField(max_length=500, blank=True, verbose_name="Сопроводительное письмо")

    class Meta:
        verbose_name_plural = "Offers"

    def __str__(self) -> str:
        return f"{self.offering} offer {self.contract}"
