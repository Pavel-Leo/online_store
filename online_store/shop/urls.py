from django.urls import path

from . import views

app_name: str = "shop"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path('feedback/', views.feedback_view, name='feedback'),
    path("delivery/", views.delivery, name="delivery"),
    path("public_offer/", views.public_offer, name="public_offer"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("how_to_buy/", views.how_to_buy, name="how_to_buy"),
    path(
        "return_and_exchange/",
        views.return_and_exchange,
        name="return_and_exchange",
    ),
    path(
        "<slug:category_slug>/",
        views.product_list,
        name="product_list_by_category",
    ),
    path("<int:id>/<slug:slug>/", views.product_detail, name="product_detail"),
]
