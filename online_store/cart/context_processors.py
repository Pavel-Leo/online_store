from typing import Dict

from .cart import Cart


def cart(request) -> Dict[str, Cart]:
    """Возвращает корзину пользователя."""
    return {'cart': Cart(request)}
