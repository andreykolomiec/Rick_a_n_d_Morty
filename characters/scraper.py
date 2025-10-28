import requests
from django.conf import settings

from characters.models import Character


#  ф-ція, яка робить запит за певним url, а потім скрапить персонажів (characters)
def scrape_characters() -> list[Character]:
    next_url_to_scrape = settings.RICK_AND_MORTY_API_CHARACTERS_URL

    # characters_response = requests.get(
    #     settings.RICK_AND_MORTY_API_CHARACTERS_URL
    # ).json()

    characters = []
    while next_url_to_scrape is not None:

        characters_response = requests.get(next_url_to_scrape).json()

        for character_dict in characters_response["results"]:
            characters.append(
                Character(
                    api_id=character_dict["id"],
                    name=character_dict["name"],
                    status=character_dict["status"],
                    species=character_dict["species"],
                    gender=character_dict["gender"],
                    image=character_dict["image"],
                )
            )
        next_url_to_scrape = characters_response["info"]["next"]
    return characters


#  ф-ція, яка зберігає всіх проскраплених персонажів (characters)
def save_characters(characters: list[Character]) -> None:
    for character in characters:
        character.save()


# ф-ція, яка з початку скрапить всіх персонажів (characters), а потім зберигає їх у БД
def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
