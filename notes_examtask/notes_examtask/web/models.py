from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="First Name",
    )

    last_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="Last Name",
    )

    age = models.IntegerField(
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Link to Profile Image"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Note(models.Model):
    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Link to Image",
    )

    content = models.TextField(
        null=False,
        blank=False,
    )
