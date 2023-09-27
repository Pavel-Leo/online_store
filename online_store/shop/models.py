from typing import Tuple

from django.db import models
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    """Модель категории товара"""
    name = models.CharField(
        max_length=200, db_index=True, verbose_name="Название"
    )
    slug = models.SlugField(
        max_length=200, unique=True, db_index=True, verbose_name="URL"
    )
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        upload_to="categories/%Y/%m/%d", blank=True, verbose_name="Изображение"
    )

    class Meta:
        ordering: Tuple[str] = ("created_at",)
        verbose_name: str = "Категория"
        verbose_name_plural: str = "Категории"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> HttpResponse:
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    """Модель товара"""
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    name = models.CharField(
        max_length=200, db_index=True, verbose_name="Название"
    )
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="URL")
    image = models.ImageField(
        upload_to="products/%Y/%m/%d",
        blank=True,
        verbose_name="Изображение",
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена"
    )
    available = models.BooleanField(default=True, verbose_name="Наличие")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата изменения"
    )

    class Meta:
        ordering: Tuple[str] = ("created",)
        index_together: Tuple[Tuple[str]] = (("id", "slug"),)
        verbose_name: str = "Продукт"
        verbose_name_plural: str = "Продукты"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> HttpResponse:
        return reverse("shop:product_detail", args=[self.id, self.slug])