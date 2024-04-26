from django.db import models
from users.models import UserModel

# Create your models here.


class CategoryModel(models.Model):
    """
    Category model.
    """

    name = models.CharField(max_length=30, verbose_name="Category")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f'Категория "{self.name}"'


class ContractModel(models.Model):
    """
    Contract model
    """

    value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Contract value")
    title = models.CharField(max_length=100, verbose_name="Contract title")
    information = models.TextField(verbose_name="Contract information")
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name="contracts",
        verbose_name="Category",
    )
    customer = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name="placed_contracts",
        verbose_name="Customer",
    )
    performer = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="completed_contracts",
        verbose_name="Performer",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date of update")
    completed = models.BooleanField(default=False, verbose_name="Выполнен")

    class Meta:
        verbose_name_plural = "Contracts"

    def __str__(self) -> str:
        return self.title
