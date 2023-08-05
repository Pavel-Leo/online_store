from typing import List, Tuple

from django import forms

PRODUCT_QUANTITY_CHOICES: List[Tuple[int, str]] = [
    (i, str(i)) for i in range(1, 21)
]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,  # видимо ошибка, найти переменную
        label="Количество",
    )
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
