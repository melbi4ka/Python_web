# Generated by Django 4.1.2 on 2022-10-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_create_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image_url', models.URLField(verbose_name='Link to Image')),
                ('content', models.TextField()),
            ],
        ),
    ]
