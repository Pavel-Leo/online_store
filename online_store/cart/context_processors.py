from typing import Dict

from .cart import Cart


def cart(request) -> Dict[str, Cart]:
    return {'cart': Cart(request)}
