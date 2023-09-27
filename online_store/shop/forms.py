from django import forms


class FeedbackForm(forms.Form):
    """Форма для отправки обратной связи."""
    question = forms.CharField(
        label="Ваш вопрос, отзыв или пожелание", widget=forms.Textarea
    )
    email = forms.EmailField(label="Адрес для получения ответа")
