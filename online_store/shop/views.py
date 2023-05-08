from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404, render

from . common import paginator_func
from .models import Category, Product

# def index(request):
#     template = "shop/shop.html"
#     title = "Главная страница"
#     context = {"title": title}
#     return render(request, template, context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).select_related('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category).select_related('category')
    cart_product_form = CartAddProductForm()
    products_list = paginator_func(request, products)
    return render(
        request,
        "shop/product/list.html",
        {
            "category": category,
            "categories": categories,
            "products_list": products_list,
            "cart_product_form": cart_product_form,
        },
    )


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "shop/product/detail.html",
        {"product": product, "cart_product_form": cart_product_form},
    )
