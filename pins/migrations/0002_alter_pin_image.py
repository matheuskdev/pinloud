# Generated by Django 5.0.2 on 2024-03-07 14:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pins", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pin",
            name="image",
            field=models.ImageField(
                upload_to="pins/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        ["PNG", "JPG", "JPEG"]
                    )
                ],
            ),
        ),
    ]
