from django.urls import path

from characters.views import get_random_characters_view

app_name = "characters"

urlpatterns = [
    path(
        "characters/random/", get_random_characters_view, name="characters_random"
    ),  # енд поінт, який повертає випадковий персонаж із серіалу «Рік і Морті».
]
