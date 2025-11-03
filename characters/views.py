from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import random
from characters.models import Character
from characters.serializers import CharacterSerializer


# створемо кастомну вюху для енд поінта, яка повертає випадковий персонаж із серіалу «Рік і Морті».


@extend_schema(responses={200: CharacterSerializer})
@api_view(["GET"])
def get_random_characters_view(request: Request) -> Response:
    """Get random character from Rick & Morty world."""
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = random.choice(pks)
    random_character = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Створимо дефолтний клас бейс вю для Кінцевої точки,
# що отримує «search_string» (рядок_пошуку) як аргумент і повертає список усіх персонажів, ім'я яких містить search_string (рядок_пошуку).


class CharacterListView(generics.ListAPIView):

    serializer_class = CharacterSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Character.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name",
                description="Filter characters by name insensitive contains",
                required=False,
                type=str,
            ),
        ]
    )
    # перевизначаємо метод get, який прописаний в ListAPIView:
    def get(self, request, *args, **kwargs) -> Response:
        """List characters with filter by name."""
        return super().get(request, *args, **kwargs)
