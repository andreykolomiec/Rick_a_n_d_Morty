from characters.models import Character
from characters.scraper import sync_characters_with_api

from celery import shared_task


# @shared_task
# def count_characters():  # Рахуємо кількість персонажів (витягуємо дані з нашої БД)
#     return Character.objects.count()


@shared_task  # тасочка (періодичне завдання), яка з початку скрапить всіх персонажів (characters), а потім зберигає їх у БД
def run_sync_with_api() -> None:
    return sync_characters_with_api()
