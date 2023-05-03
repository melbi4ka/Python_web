# Generated by Django 4.1.2 on 2022-10-22 19:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_game_max_level_alter_game_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='max_level',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Max level cannot be below 1.')]),
            preserve_default=False,
        ),
    ]
