# Generated by Django 4.1.2 on 2022-10-22 07:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_create_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(choices=[('Act', 'Action'), ('Adv', 'Adventure'), ('Pzl', 'Puzzle'), ('Stg', 'Strategy'), ('Spr', 'Sports'), ('Crd', 'Board/Card Game'), ('Oth', 'Other')], max_length=15)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1), django.core.validators.MaxValueValidator(5.0)])),
                ('max_level', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('game_img', models.URLField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
