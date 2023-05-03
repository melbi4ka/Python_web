from django.core import validators, exceptions
from django.db import models

from my_musicapp.web.validators import validate_name_chatracters


class Profile(models.Model):
    NAME_MIN_LEN = 2

    username = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators = (
            validators.MinLengthValidator(NAME_MIN_LEN),
            validate_name_chatracters,
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,

    )


class Album(models.Model):
    MIN_PRICE = 0

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER = "Other"

    GENRE_CHOISES = (
        (POP_MUSIC,POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER, OTHER),
    )

    album_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices= GENRE_CHOISES
    )

    description = models.TextField(
        null=True,
        blank=True,

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

    class Meta:
        ordering = ['pk']





