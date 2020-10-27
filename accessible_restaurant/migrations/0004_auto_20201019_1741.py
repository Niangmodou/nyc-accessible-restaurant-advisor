# Generated by Django 3.1.2 on 2020-10-19 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accessible_restaurant", "0003_auto_20201018_1752"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant_profile",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rprofile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="user_profile",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="uprofile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]