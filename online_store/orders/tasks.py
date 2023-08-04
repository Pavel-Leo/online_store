import os

# from celery import shared_task
from django.core.mail import send_mail
from dotenv import load_dotenv

from .models import Order

load_dotenv()

APP_EMAIL = os.getenv("EMAIL_HOST_USER")


# @shared_task
def order_created(order_id):
    """
    Задание по отправке уведомления по электронной почте
    при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Заказ № {order.id}"
    message = (
        f"Дорогой {order.Имя},\n\n"
        "Ваш заказ успешно оформлен. "
        f"Номер Вашего заказа: {order.id}."
    )
    mail_sent = send_mail(
        subject,
        message,
        "fionit.2079@gmail.com",
        [order.email, "fionit.2079@gmail.com"],
    )
    return mail_sent
