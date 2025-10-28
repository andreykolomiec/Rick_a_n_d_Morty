from django.db import models


class Character(models.Model):
    class StatusChoices(models.TextChoices):
        ALIVE = "Alive"
        DEAD = "Dead"
        UNKNOWN = "unknown"

    class GenderChoices(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        GENDERLESS = "Genderless"
        UNKNOWN = "unknown"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=StatusChoices.choices)
    species = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GenderChoices.choices)
    image = models.URLField(max_length=200, unique=True)

    def __str__(self):
        return self.name
