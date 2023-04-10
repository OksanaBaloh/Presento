# Generated by Django 4.1.7 on 2023-04-10 08:03

from django.db import migrations, models
import gift.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gift",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=9)),
                ("description", models.TextField()),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Both", "Both"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=gift.models.gift_image_file_path,
                    ),
                ),
                (
                    "age",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("0-16", "Under 16"),
                            ("17-25", "Between 17 25"),
                            ("26-45", "Between 26 45"),
                            ("46-100", "Over 45"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "occasion",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Birthday", "Birthday"),
                            ("Wedding", "Wedding"),
                            ("New Year", "New Year"),
                            ("Valentines Day", "Valentines Day"),
                            ("Graduation", "Graduation"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "likes",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("IT", "It"),
                            ("Beauty", "Beauty"),
                            ("Sport", "Sport"),
                            ("Cars", "Cars"),
                            ("Fashion", "Fashion"),
                            ("Music", "Music"),
                        ],
                        max_length=15,
                    ),
                ),
            ],
        ),
    ]
