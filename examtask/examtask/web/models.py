from django.core import validators, exceptions
from django.db import models


def model_year_validator(value):
    if value < 1980 or value > 2049:
        raise exceptions.ValidationError("Year must be between 1980 and 2049")


def min_name_validator(value):
    if value < 2:
        raise exceptions.ValidationError("The username must be a minimum of 2 chars")


class Profile(models.Model):
    MAX_LEN_NAME = 10
    MIN_LEN_NAME = 2
    MIN_AGE = 18

    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_AGE),
        )
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name or self.last_name:
            if self.first_name:
                return f"{self.first_name}"
            else:
                return f"{self.last_name}"
        else:
            return None


class Car(models.Model):
    MAX_MODEL_LEN = 20
    MIN_MODEL_LEN = 2

    MAX_TYPE_LEN = 10
    MIN_PRICE = 1.0

    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"
    CAR_CHOISES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )
    type = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_TYPE_LEN,
        choices=CAR_CHOISES,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_MODEL_LEN,
        validators=(
            validators.MinLengthValidator(MIN_MODEL_LEN),
        )
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            model_year_validator,
        )
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        )
    )
