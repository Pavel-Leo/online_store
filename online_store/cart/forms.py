from typing import List, Tuple

from django import forms

PRODUCT_QUANTITY_CHOICES: List[Tuple[int, str]] = [
    (i, str(i)) for i in range(1, 21)
]


class CartAddProductForm(forms.Form):
    """Форма добавления товара в корзину по количеству."""
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        label="Количество",
    )
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
