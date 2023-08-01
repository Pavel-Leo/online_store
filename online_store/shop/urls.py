from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("contacts/", views.contacts, name="contacts"),
    path('feedback/', views.feedback_view, name='feedback'),
    path("delivery/", views.delivery, name="delivery"),
    path(
        "<slug:category_slug>/",
        views.product_list,
        name="product_list_by_category",
    ),
    path("<int:id>/<slug:slug>/", views.product_detail, name="product_detail"),

]
