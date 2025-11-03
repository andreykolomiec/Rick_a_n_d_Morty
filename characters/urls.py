from django.urls import path

from characters.views import get_random_characters_view, CharacterListView

app_name = "characters"

urlpatterns = [
    path(
        "characters/random/", get_random_characters_view, name="characters_random"
    ),  # енд поінт, який повертає випадковий персонаж із серіалу «Рік і Морті».
    path(
        "characters/", CharacterListView.as_view(), name="characters_list"
    ),  # Кінцева точка, що отримує «search_string» (рядок_пошуку) як аргумент і повертає список усіх персонажів, ім'я яких містить search_string (рядок_пошуку).
]
