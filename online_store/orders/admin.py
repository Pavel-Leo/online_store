from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "Имя",
        "Фамилия",
        "email",
        "Адрес",
        "Индекс",
        "Город",
        "paid",
        "created",
        "updated",
    ]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInline]
