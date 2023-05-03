import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "online_store.settings")
app = Celery("online_store")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
