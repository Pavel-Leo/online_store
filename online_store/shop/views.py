from multiprocessing import context
from typing import Dict

from cart.forms import CartAddProductForm
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from shop.forms import FeedbackForm

from .common import paginator_func
from .models import Category, Product

PRODUCT_CATEGORIES = [
    "Кофе молотый",
    "Кофе зерновой",
    "Чай черный листовой",
    "Чай зеленый листовой",
]


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).select_related(
        'category'
    )
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category).select_related(
            'category'
        )
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


def product_detail(request, id, slug) -> HttpResponse:
    product: Product = get_object_or_404(
        Product, id=id, slug=slug, available=True
    )
    categories: Category = Category.objects.all()
    cart_product_form: CartAddProductForm = CartAddProductForm()
    if product.category.name in PRODUCT_CATEGORIES:
        cat_1: Category = get_object_or_404(Category, name="Посуда")
        cat_2: Category = get_object_or_404(Category, name="Кофемолки")
        cat_3: Category = get_object_or_404(Category, name="Контейнеры")
    else:
        cat_1: Category = get_object_or_404(Category, name="Кофе зерновой")
        cat_2: Category = get_object_or_404(Category, name="Кофе молотый")
        cat_3: Category = get_object_or_404(
            Category, name="Чай черный листовой"
        )
    context: Dict[str, Category] = {
        "cat_1": cat_1,
        "cat_2": cat_2,
        "cat_3": cat_3,
        "product": product,
        "cart_product_form": cart_product_form,
        "categories": categories,
    }
    return render(request, "shop/product/detail.html", context)


def about(request) -> HttpResponse:
    categories: Category = Category.objects.all()
    context: Dict[str, Category] = {"categories": categories}
    return render(request, "about/about.html", context)


def contacts(request) -> HttpResponse:
    categories: Category = Category.objects.all()
    context: Dict[str, Category] = {"categories": categories}
    return render(request, "contacts/contacts.html", context)


def delivery(request) -> HttpResponse:
    categories: Category = Category.objects.all()
    context: Dict[str, Category] = {"categories": categories}
    return render(request, "about/delivery.html", context)


def public_offer(request) -> HttpResponse:
    categories: Category = Category.objects.all()
    context: Dict[str, Category] = {"categories": categories}
    return render(request, "about/public_offer.html", context)


def privacy_policy(request) -> HttpResponse:
    categories: Category = Category.objects.all()
    context: Dict[str, Category] = {"categories": categories}
    return render(request, "about/privacy_policy.html", context)


def how_to_buy(request) -> HttpResponse:
    categories: Category = Category.objects.all()
    context: Dict[str, Category] = {"categories": categories}
    return render(request, "about/how_to_buy.html", context)


def return_and_exchange(request) -> HttpResponse:
    categories: Category = Category.objects.all()
    context: Dict[str, Category] = {"categories": categories}
    return render(request, "about/return_and_exchange.html", context)


def feedback_view(request) -> HttpResponse:
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            email = form.cleaned_data['email']
            subject: str = 'Обратная связь от пользователя'
            message: str = (
                f'Вопрос/Отзыв/Пожелание: {question}\nАдрес для ответа:'
                f' {email}'
            )
            from_email = settings.EMAIL_HOST_USER
            to_email = [settings.EMAIL_HOST_USER]
            send_mail(
                subject, message, from_email, to_email, fail_silently=False
            )
            return render(request, 'contacts/success.html', {'form': form})
    else:
        form = FeedbackForm()
    return render(request, 'contacts/contacts.html', {'form': form})
