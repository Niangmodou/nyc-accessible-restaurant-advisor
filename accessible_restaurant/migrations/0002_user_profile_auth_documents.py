# Generated by Django 3.1.2 on 2020-11-07 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accessible_restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_profile",
            name="auth_documents",
            field=models.FileField(
                default="documents/pdfs/test.pdf", upload_to="documents/pdfs/"
            ),
        ),
    ]
