from django.db import models
from shop.models import Product


class Order(models.Model):
    Имя = models.CharField(max_length=50)
    Фамилия = models.CharField(max_length=50)
    email = models.EmailField()
    Адрес = models.CharField(max_length=250)
    Индекс = models.CharField(max_length=20)
    Город = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    stripe_id = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ("-created",)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return "Order {}".format(self.id)

    def get_total_cost(self):
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

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
