# Generated by Django 4.2.10 on 2024-02-24 04:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_basket"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]