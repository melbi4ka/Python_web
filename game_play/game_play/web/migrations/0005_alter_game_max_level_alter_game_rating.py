# Generated by Django 4.1.2 on 2022-10-22 09:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='max_level',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1, message='Max level cannot be below 1.')]),
        ),
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.1, message='Rating can be between 0.1 and 5.0'), django.core.validators.MaxValueValidator(5.0, message='Rating can be between 0.1 and 5.0')]),
        ),
    ]