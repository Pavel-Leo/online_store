from typing import List

from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields: List[str] = [
            "Имя",
            "Фамилия",
            "email",
            "Адрес",
            "Индекс",
            "Город",
        ]
