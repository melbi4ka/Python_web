from django.db import models

class Recipe(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    ingredients = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )

    time = models.PositiveIntegerField(
        null=False,
        blank=True,
    )

    class Meta:
        ordering = ("id", )

