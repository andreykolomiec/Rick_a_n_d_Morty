# Це гарантує, що додаток завжди імпортується під час запуску Django,
# щоб shared_task (спільне завдання) використовувало цей додаток.
from .celery import app as celery_app

__all__ = ("celery_app",)
