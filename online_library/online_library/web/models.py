from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    profile_img = models.URLField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Book(models.Model):
    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
