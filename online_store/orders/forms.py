from typing import List

from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    """Форма создания заказа."""
    class Meta:
        model = Order
        fields: List[str] = [
            "name",
            "last_name",
            "email",
            "adress",
            "postal_code",
            "city",
        ]
