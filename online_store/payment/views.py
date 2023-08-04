import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render, reverse
from orders.models import Order
from shop.models import Category

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def payment_process(request):
    order_id = request.session.get("order_id", None)
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        success_url = request.build_absolute_uri(reverse("payment:completed"))
        cancel_url = request.build_absolute_uri(reverse("payment:canceled"))
        session_data = {
            "mode": "payment",
            "client_reference_id": order.id,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "line_items": [],
        }
        for item in order.items.all():
            session_data["line_items"].append(
                {
                    "price_data": {
                        "currency": "RUB",
                        "product_data": {"name": item.product.name},
                        "unit_amount": int(item.price * 100),
                    },
                    "quantity": item.quantity,
                }
            )
        session = stripe.checkout.Session.create(**session_data)
        return redirect(session.url, code=303)
    else:
        return render(request, "payment/process.html", locals())


def payment_completed(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "payment/completed.html", context)


def payment_canceled(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "payment/canceled.html", context)
