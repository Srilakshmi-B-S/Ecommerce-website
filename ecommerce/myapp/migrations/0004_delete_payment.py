# Generated by Django 5.0.6 on 2024-07-11 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_payment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Payment",
        ),
    ]
