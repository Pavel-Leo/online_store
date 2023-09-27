import decimal
from decimal import Decimal

from django.conf import settings
from shop.models import Product


class Cart(object):
    """Класс для работы с корзиной."""

    def __init__(self, request) -> None:
        """Инициализация объекта корзины."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False) -> None:
        """Добавление товара в корзину или обновление его количества."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(product.price),
            }
        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def save(self) -> None:
        self.session.modified = True

    def remove(self, product) -> None:
        """Удаление товара из корзины."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Перебор корзины."""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"]: decimal = Decimal(item["price"])
            item["total_price"]: decimal = item["price"] * item["quantity"]
            yield item

    def __len__(self) -> int:
        """Возвращает общее количество товаров в корзине."""
        return len(self.cart)

    def get_total_price(self) -> Decimal:
        """Возвращает общую стоимость товаров в корзине."""
        return sum(
            Decimal(item["price"]) * item["quantity"]
            for item in self.cart.values()
        )

    def clear(self) -> None:
        """Очищение корзины."""
        del self.session[settings.CART_SESSION_ID]
        self.save()
