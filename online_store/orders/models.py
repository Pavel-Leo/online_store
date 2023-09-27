import decimal
from typing import Tuple

from django.db import models
from shop.models import Product


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField()
    adress = models.CharField(max_length=250, verbose_name="Адрес")
    postal_code = models.CharField(max_length=20, verbose_name="Индекс")
    city = models.CharField(max_length=100, verbose_name="Город")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    stripe_id = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering: Tuple[str] = ("-created",)
        verbose_name: str = "Заказ"
        verbose_name_plural: str = "Заказы"

    def __str__(self) -> str:
        return "Order {}".format(self.id)

    def get_total_cost(self) -> int:
        return sum(item.get_cost() for item in self.items.all()) + 350


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return str(self.id)

    def get_cost(self) -> decimal:
        return self.price * self.quantity
