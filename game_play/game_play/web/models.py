from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    MIN_AGE_VALUE = 12

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_AGE_VALUE, message="Age must be over 12"),
        )
    )

    password = models.CharField(
        null=False,
        blank=True,
        max_length=30,

    )
    first_name = models.CharField(
        null = True,
        blank=True,
        max_length=30,
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    profile_img = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return f"{self.first_name}"
        elif self.last_name:
            return f"{self.last_name}"
        else:
            return None

class Game(models.Model):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS="Sports"
    CARD_GAME = "Board/Card Game"
    OTHER = "Other"

    GAME_CHOICES = [
        (ACTION, "Action"),
        (ADVENTURE, "Adventure"),
        (PUZZLE, "Puzzle"),
        (STRATEGY, "Strategy"),
        (SPORTS, "Sports"),
        (CARD_GAME, "Board/Card Game"),
        (OTHER, "Other"),
    ]

    MIN_VALUE_RATING = 0.1
    MAX_VALUE_RATING = 5.0

    MIN_VALUE_LEVEL = 1

    title = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=15,
        choices=GAME_CHOICES,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators = (
            MinValueValidator(MIN_VALUE_RATING,
                              message=f"Rating can be between "
                                      f"{MIN_VALUE_RATING} and {MAX_VALUE_RATING}"),
            MaxValueValidator(MAX_VALUE_RATING,
                              message=f"Rating can be between "
                                      f"{MIN_VALUE_RATING} and {MAX_VALUE_RATING}"),
        )
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_VALUE_LEVEL,
                              message=f"Max level cannot be below {MIN_VALUE_LEVEL}."),
                    )
    )

    game_img = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )







