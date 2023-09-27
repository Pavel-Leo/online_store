from typing import Dict

from django.shortcuts import (
    HttpResponse,
    HttpResponseRedirect,
    get_object_or_404,
    redirect,
    render,
)
from django.views.decorators.http import require_POST
from shop.models import Category, Product

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id) -> HttpResponseRedirect:
    """Функция для добавления товара в корзину."""
    cart: Cart = Cart(request)
    product: Product = get_object_or_404(Product, id=product_id)
    form: CartAddProductForm = CartAddProductForm(request.POST)
    if form.is_valid():
        cd: Dict[str, int] = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd["quantity"],
            override_quantity=True,
        )
        return redirect("cart:cart_detail")


def cart_remove(request, product_id) -> HttpResponseRedirect:
    """Функция для удаления товара из корзины."""
    cart: Cart = Cart(request)
    product: Product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail(request) -> HttpResponse:
    """Функция для отображения содержимого корзины."""
    cart: Cart = Cart(request)
    categories: Category = Category.objects.all()
    context: Dict[str, any] = {"categories": categories, "cart": cart}
    for item in cart:
        item["update_quantity_form"] = CartAddProductForm(
            initial={"quantity": item["quantity"], "override": True}
        )
    return render(request, "cart/detail_cart.html", context)
