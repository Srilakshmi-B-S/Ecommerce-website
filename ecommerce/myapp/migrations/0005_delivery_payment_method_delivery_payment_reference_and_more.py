# Generated by Django 5.0.6 on 2024-07-18 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_delete_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="delivery",
            name="payment_method",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="delivery",
            name="payment_reference",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="delivery",
            name="payment_status",
            field=models.CharField(default="Pending", max_length=50),
        ),
    ]
