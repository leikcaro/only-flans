# Generated by Django 5.0.6 on 2024-06-05 23:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_rename_descripcion_flan_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactForm",
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
                (
                    "contact_form_uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                ("customer_email", models.EmailField(max_length=254)),
                ("customer_name", models.CharField(max_length=64)),
                ("message", models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name="cliente",
            old_name="edad",
            new_name="age",
        ),
        migrations.RenameField(
            model_name="cliente",
            old_name="apellidos",
            new_name="lastname",
        ),
        migrations.RenameField(
            model_name="cliente",
            old_name="mensaje",
            new_name="message",
        ),
        migrations.RenameField(
            model_name="cliente",
            old_name="nombres",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="cliente",
            old_name="asunto",
            new_name="subject",
        ),
    ]
