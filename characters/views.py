from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import random
from characters.models import Character
from characters.serializers import CharacterSerializer


# створемо кастомну вюху для енд поінта, яка повертає випадковий персонаж із серіалу «Рік і Морті».
@api_view(["GET"])
def get_random_characters_view(request: Request) -> Response:
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = random.choice(pks)
    random_character = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Створимо дефолтний клас бейс вю для Кінцевої точки,
# що отримує «search_string» як аргумент і повертає список усіх персонажів, ім'я яких містить search_string.
