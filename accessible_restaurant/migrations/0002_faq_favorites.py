# Generated by Django 3.1.2 on 2020-12-01 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accessible_restaurant", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FAQ",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=128)),
                ("answer", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Favorites",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorite",
                        to="accessible_restaurant.restaurant",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorite",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]