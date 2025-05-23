# Generated by Django 5.2.1 on 2025-05-10 23:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("title", models.CharField()),
                ("subtitle", models.CharField()),
                ("short_description", models.CharField()),
                ("description", models.CharField()),
                ("image_url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="ServiceFeature",
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
                ("value", models.CharField()),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service.service",
                    ),
                ),
            ],
        ),
    ]
