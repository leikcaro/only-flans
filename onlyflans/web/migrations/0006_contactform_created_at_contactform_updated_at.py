# Generated by Django 5.0.6 on 2024-06-07 04:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0005_rename_email_contactform_customer_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactform",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="contactform",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
