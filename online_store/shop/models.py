from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE, verbose_name="Категория"
    )
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="URL")
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True, verbose_name="Изображение",)
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.FloatField(default=0, verbose_name="Цена")
    available = models.BooleanField(default=True, verbose_name="Наличие")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])

    def __str__(self):
        return self.name
